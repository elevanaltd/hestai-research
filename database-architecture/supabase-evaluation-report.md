# Platform Evaluation Report – Supabase vs Alternatives for Innovation Infrastructure
**Date:** 2025-06-15

## Executive Summary

This report evaluates whether Supabase is the most robust and appropriate backend platform for supporting a video production and translation system involving three major innovations: Modular Scene-Based Production Framework, Parallel Quest Architecture, and TranslationFlow Platform. The comparison includes Firebase, PlanetScale, Neon, and DynamoDB, focusing on relational data requirements, global collaboration (UK ↔ US), and semi-real-time workflow enablement.

---

## Key Findings

### ✅ Supabase – Best Overall Fit

Supabase is strongly suited to Shaun’s use case, offering:
- Full **PostgreSQL relational structure**
- Row-Level Security (RLS) and integrated **Auth + Storage**
- REST and optional **GraphQL** APIs
- Real-time updates via logical replication (sufficient for <24h sync)
- Good developer ergonomics and flexible pricing (~$29–$79/mo)

### 🟡 PlanetScale – Best for Global Read Latency and Uptime

Built on Vitess (MySQL), PlanetScale is:
- Highly performant with **five-nines uptime**
- Designed for **global reads and branching**
- Requires external auth, storage, real-time sync layers

### 🟠 Firebase – Best for Real-Time Mobile Use, Not Relational

Firestore shines in:
- Sub-second real-time sync
- Built-in auth, hosting, and offline cache
- Poor relational support (joins, consistency)

### 🟣 Neon – Emerging Option for Serverless Postgres

Neon offers:
- PostgreSQL with branching and serverless scaling
- Good for dev/test environments
- Still maturing for multi-region real-time use

---

## Collaboration & Real-Time Fit

| Platform       | Global (UK–US) Sync | Semi-Real-Time Suitability | Real Relational? | Built-in Auth + Storage |
|----------------|---------------------|-----------------------------|------------------|--------------------------|
| **Supabase**   | ✅ Yes (eu-west + us-east) | ✅ Hours-level updates    | ✅ Yes (Postgres) | ✅ Yes                   |
| **PlanetScale**| ✅ Excellent         | ⚠️ Manual via 3rd-party    | ✅ Yes (MySQL)    | ❌ No                    |
| **Firebase**   | ✅ Excellent         | ✅ Best-in-class            | ❌ No             | ✅ Yes                   |
| **Neon**       | ⚠️ In development    | ⚠️ Possible with tooling    | ✅ Yes (Postgres) | ❌ No                    |

---

## Innovation Alignment Summary

### Innovation 1: Modular Scene-Based Production

- **Supabase Fit:** Excellent
- Maps cleanly to relational structure: `scenes`, `videos`, `checklists`, `notes`, `users`
- Supports mobile operator workflows and checklist updates via API

### Innovation 2: Parallel Quest Architecture

- **Supabase Fit:** Strong
- Dynamic task/quest tracking via Postgres schema + triggers or Edge Functions
- RLS can enforce user-specific access to quests

### Innovation 3: TranslationFlow Platform

- **Supabase Fit:** Good
- Requires layering in Pusher/Ably for collaborative real-time sentence editing
- PostgreSQL suitable for sentence/audiotrack linking, feedback, timing alignment

---

## Final Recommendation

| Requirement                                  | Best Platform         |
|---------------------------------------------|-----------------------|
| Relational workflows + global access         | ✅ Supabase           |
| Fast onboarding + templated scenes           | ✅ Supabase           |
| Sub-second real-time sync                    | ❌ Supabase (needs extension) |
| Global read latency (US/UK)                  | ✅ Supabase or PlanetScale |
| Complex modular workflows                    | ✅ Supabase           |
| Open-source and self-hosting path            | ✅ Supabase           |

### Recommendation:
Use **Supabase as the primary backend**, layering in third-party tools for enhanced real-time sync or automation as needed.

---

## Next Steps
- Scaffold schema for Innovations 1 & 2
- Set up Edge Functions or n8n for variable-triggered workflow
- Consider Liveblocks or Ably for collaborative editing (Innovation 3)
- Monitor Supabase region options for potential latency tuning

