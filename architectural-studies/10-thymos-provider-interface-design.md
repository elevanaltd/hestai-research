# A-001: Provider Interface Layer Design

## Question Reference
How should we implement the provider interface layer to ensure proper abstraction between different LLM providers (OpenAI, Anthropic, Google) while maintaining flexibility for tier-based model selection?

## Answer

Based on MVP testing results and empirical evidence, we recommend a **Configuration-Driven Direct SDK Approach** for the provider interface layer, replacing the previously considered LiteLLM solution which demonstrated instability in our testing environment.

### Core Architecture

```
┌──────────────┐
│   Thymos UI  │  (role & tier selection, model configuration)
└──────┬───────┘
       │ HTTP / API
┌──────▼──────────────────────────────────────────────────────┐
│          Thymos Backend                                     │
│  • Role system (Zeus, Hermes, etc.)                         │
│  • Tier mapping (Gold, Silver, Bronze)                      │
│  • Configuration-driven parameter mapping                    │
│  • Native provider SDK integration                          │
└──────┬─────────────┬──────────────────┬────────────────────┘
       │             │                  │
 ┌─────▼────┐  ┌─────▼─────┐     ┌──────▼─────┐
 │ OpenAI   │  │ Anthropic │     │ Google     │
 │ Native   │  │ Native    │     │ Native     │
 │ SDK      │  │ SDK       │     │ SDK        │
 └──────────┘  └───────────┘     └────────────┘
```

### Implementation Approach

Our MVP testing revealed critical instabilities with middleware proxy solutions like LiteLLM, particularly with OpenAI models which would complete successfully but crash during post-processing. This finding leads us to recommend a direct SDK approach with a configuration-driven parameter mapping system.

1. **Configuration-Driven Parameter Mapping**:

```python
# Database-stored configuration (not hardcoded)
PROVIDER_MAPS = {
    "openai": {
        "input_map": {
            "prompt": lambda p: {"messages": [{"role": "user", "content": p}]},
            "temperature": lambda t: {"temperature": t},
            "max_tokens": lambda m: {"max_tokens": m}
        },
        "output_map": {
            "text": lambda r: r.choices[0].message.content,
            "usage": lambda r: r.usage.to_dict()
        }
    },
    "anthropic": {
        "input_map": {
            "prompt": lambda p: {"messages": [{"role": "user", "content": p}]},
            "temperature": lambda t: {"temperature": t},
            "max_tokens": lambda m: {"max_tokens": m}
        },
        "output_map": {
            "text": lambda r: r.content[0].text,
            "usage": lambda r: {"prompt_tokens": r.usage.input_tokens, 
                              "completion_tokens": r.usage.output_tokens}
        }
    }
}
```

2. **Minimal Provider Interface**:

```python
async def generate(
    prompt: str,
    role: str,
    tier: str,
    core_params: dict = {},
    provider_params: dict = {}
):
    """
    Generate text using role-tier configuration with proper provider selection.
    
    Arguments:
        prompt: The input text to process
        role: Role identifier (zeus, hermes, etc.)
        tier: Tier level (gold, silver, bronze)
        core_params: Standard parameters that work across providers
        provider_params: Provider-specific parameters that bypass mapping
    """
    # Get model configuration for role/tier
    config = await get_role_tier_config(role, tier)
    provider = config["provider"]
    model = config["model"]
    
    # Apply parameter mapping for the selected provider
    mapped_params = {}
    for param, value in core_params.items():
        if param in PROVIDER_MAPS[provider]["input_map"]:
            mapper = PROVIDER_MAPS[provider]["input_map"][param]
            mapped_params.update(mapper(value))
    
    # Add provider-specific parameters directly
    mapped_params.update(provider_params)
    
    # Call the appropriate native SDK
    try:
        if provider == "openai":
            response = await call_openai(model, mapped_params)
        elif provider == "anthropic":
            response = await call_anthropic(model, mapped_params)
        elif provider == "google":
            response = await call_google(model, mapped_params)
        
        # Map response to standardized format
        result = {}
        for key, mapper in PROVIDER_MAPS[provider]["output_map"].items():
            result[key] = mapper(response)
        
        result["provider"] = provider
        result["model"] = model
        
        return result
    except Exception as e:
        # Handle fallback if available
        if "fallbacks" in config and config["fallbacks"]:
            fallback = config["fallbacks"][0]
            return await generate(
                prompt, 
                role, 
                tier, 
                core_params, 
                provider_params,
                _fallback_attempt=True
            )
        else:
            raise e
```

3. **Database Schema for Configuration**:

```sql
CREATE TABLE models (
    id VARCHAR(50) PRIMARY KEY,
    display_name VARCHAR(100) NOT NULL,
    provider VARCHAR(50) NOT NULL,
    model_identifier VARCHAR(100) NOT NULL,
    capabilities JSONB,
    token_limit INTEGER,
    cost_per_token NUMERIC(10, 8),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE role_tier_assignments (
    id SERIAL PRIMARY KEY,
    role VARCHAR(50) NOT NULL,
    tier VARCHAR(20) NOT NULL,
    model_id VARCHAR(50) REFERENCES models(id),
    fallback_models JSONB, -- Array of fallback model IDs
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(role, tier)
);
```

### UI for Model Management

The database-backed configuration enables a comprehensive UI for model management:

```jsx
// Model Configuration Page
function ModelConfigurationPage() {
  const [roles, setRoles] = useState([]);
  const [tiers, setTiers] = useState([]);
  const [models, setModels] = useState([]);
  const [assignments, setAssignments] = useState({});
  
  // Fetch configuration data
  useEffect(() => {
    async function loadConfig() {
      const [rolesData, tiersData, modelsData, assignmentsData] = await Promise.all([
        fetch('/api/roles').then(r => r.json()),
        fetch('/api/tiers').then(r => r.json()),
        fetch('/api/models').then(r => r.json()),
        fetch('/api/role-tier-assignments').then(r => r.json())
      ]);
      
      setRoles(rolesData);
      setTiers(tiersData);
      setModels(modelsData);
      
      // Transform assignments into a lookup structure
      const assignmentMap = {};
      assignmentsData.forEach(a => {
        if (!assignmentMap[a.role]) assignmentMap[a.role] = {};
        assignmentMap[a.role][a.tier] = {
          modelId: a.model_id,
          fallbacks: a.fallback_models || []
        };
      });
      setAssignments(assignmentMap);
    }
    
    loadConfig();
  }, []);
  
  // Update model assignment
  async function updateAssignment(role, tier, modelId, fallbacks = []) {
    await fetch(`/api/role-tier-assignments/${role}/${tier}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model_id: modelId, fallback_models: fallbacks })
    });
    
    // Update local state
    setAssignments(prev => ({
      ...prev,
      [role]: {
        ...prev[role],
        [tier]: { modelId, fallbacks }
      }
    }));
  }
  
  return (
    <div className="model-configuration">
      <h1>Model Configuration</h1>
      
      <table>
        <thead>
          <tr>
            <th>Role</th>
            {tiers.map(tier => (
              <th key={tier.id}>{tier.display_name}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {roles.map(role => (
            <tr key={role.id}>
              <td>{role.display_name}</td>
              {tiers.map(tier => (
                <td key={`${role.id}-${tier.id}`}>
                  <select
                    value={assignments[role.id]?.[tier.id]?.modelId || ''}
                    onChange={e => updateAssignment(
                      role.id, 
                      tier.id, 
                      e.target.value,
                      assignments[role.id]?.[tier.id]?.fallbacks || []
                    )}
                  >
                    <option value="">-- Select Model --</option>
                    {models
                      .filter(m => m.status === 'active')
                      .map(model => (
                        <option key={model.id} value={model.id}>
                          {model.display_name}
                        </option>
                      ))}
                  </select>
                  
                  {/* Fallback configuration UI would go here */}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

## Implementation Considerations

Our recommendation to switch from LiteLLM to a configuration-driven direct SDK approach is based on several key factors:

### 1. Reliability Issues with Proxy Solutions

The MVP testing demonstrated significant reliability issues with proxy middleware approaches like LiteLLM:
- OpenAI models completed model calls successfully but crashed in post-processing
- This created opaque failure patterns difficult to debug and fix
- Direct SDK calls provide cleaner error boundaries and more predictable behavior

### 2. Enhanced Flexibility

A configuration-driven approach provides several advantages:
- Complex provider-specific features can be directly accessed when needed
- Parameter mapping is explicit and maintainable through configuration
- New providers can be added without complex middleware updates
- Simplified upgrade path when provider SDKs are updated

### 3. MPE Alignment

This approach aligns with Minimal Philosopher-Engineer principles:
- Preserves essential complexity (provider differences) while minimizing accumulative complexity (perfect abstraction)
- Uses constraints as generative boundaries, not limitations
- Balances standardization (core parameters) with direct access (provider-specific features)
- Enables evolution through configuration rather than code changes

### 4. RAPH Integration Support

The direct SDK approach better supports RAPH sequential processing:
- Allows tier-appropriate models for each RAPH stage
- Enables direct control over model parameters for specialized tasks
- Provides more predictable error handling for multi-stage processing
- Better supports the capsule storage and retrieval patterns needed for RAPH

## Implementation Strategy

1. **Initial Database Setup**
   - Implement the configuration schema
   - Create admin interfaces for configuration management
   - Populate with initial models and configurations

2. **Core Provider Interface**
   - Implement direct SDK integrations for primary providers
   - Create the parameter mapping system
   - Build the generate() function with fallback support

3. **UI Development**
   - Build model configuration interface
   - Implement role-tier assignment management
   - Create provider monitoring dashboard

4. **Testing and Validation**
   - Test all providers with various parameters
   - Validate fallback behavior
   - Benchmark performance and reliability

## Conclusion

Based on empirical evidence from MVP testing, we recommend a configuration-driven direct SDK approach for the provider interface layer. This approach offers improved reliability, clearer error boundaries, and better support for specialized features while maintaining the flexibility of a proper abstraction layer.

The database-backed configuration system ensures a single source of truth for model assignments and enables a comprehensive user interface for model management. This approach meets all three key requirements:

1. A complete list of all available models is visible in the UI
2. Adding new models is simple through a single configuration interface
3. A model configuration page allows assignment of models to all 24 role-tier combinations

This architecture provides a solid foundation that will grow with the system while avoiding the reliability issues observed with middleware proxy solutions.
