# Exam AI-901 Study Plan & Progress Tracker

- **Exam:** AI-901 — Microsoft Certified: Azure AI Fundamentals
- **Passing Score:** 700 / 1000
- **Expiration:** Fundamentals certifications do not expire
- **RAG Knowledge Index:** [../KNOWLEDGE_INDEX.md](../KNOWLEDGE_INDEX.md)
- **Target Exam Date:** *(TBD — update once scheduled)*

---

## Foundations & Architecture (Completed Imports)
Notes folder: [00-foundations-and-roadmap/](00-foundations-and-roadmap/)
- [x] Full-stack portfolio roadmap (Shipkit.ai + FastAPI + Supabase + Microsoft Foundry)
- [x] Python virtual environments (`.venv`) & workspace hygiene
- [x] REST APIs, HTTP headers, JSON payloads, and Voice-Agent SaaS concepts
- [x] Identified hands-on Python SDK focus plan (`azure-ai-textanalytics` lab)

---

## Domain 1: Identify AI Concepts and Capabilities (40–45%)
Notes folder: [01-ai-concepts/](01-ai-concepts/README.md)

- [ ] **1.1 Responsible AI Principles**
  - Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, Accountability
  - *Finance/QA lens:* Bias auditing, hallucination testing, PII redaction, compliance guardrails
- [ ] **1.2 Core Model Concepts & Configuration**
  - Tokens, context windows, prompts (system vs. user), embeddings, temperature / top-p, grounding (RAG)
- [ ] **1.3 AI Workloads & Scenarios**
  - Generative AI vs. Agentic AI (single-agent workflows, tools, memory)
  - Natural Language Processing (NLP), Speech, Computer Vision, and Information Extraction

---

## Domain 2: Implement AI Solutions Using Microsoft Foundry (55–60%)
Notes folder: [02-foundry-solutions/](02-foundry-solutions/README.md)

- [x] **2.1 Microsoft Foundry Basics, Setup & Azure RBAC**
  - Foundry vs. Azure OpenAI endpoints, `az login`, least-privilege Azure RBAC (Foundry IQ, Templates, Models, Dev Packs)
- [ ] **2.2 Model Catalog & Deployment**
  - Selecting, deploying, testing, and configuring foundational LLMs & multimodal models
- [x] **2.3 Building Single-Agent Solutions (Foundations)**
  - Stateless models vs. stateful Foundry Agents, `get_openai_client`, `conversations.create()`, `responses.create()`
  - [x] Interactive multi-turn `while` loop implemented across `poc1-starter`, `expenses-agent`, and `text-to-image-agent`
- [ ] **2.4 Text, Speech, Vision & Information Extraction**
  - [x] *Lab scaffolded:* `agents/banking-qa-text-analyzer` (`azure-ai-textanalytics` — PII redaction, sentiment, key phrases)
  - [ ] Install `azure-ai-textanalytics` and run live test
  - [ ] Document Intelligence / Azure Content Understanding
- [ ] **2.5 Reading Basic Python & REST/SDK Snippets**
  - Imports, `.env` variables, `AIProjectClient`, REST headers/JSON payloads, Entra ID (`DefaultAzureCredential`)

---

## Hands-On Portfolio Milestones (Resume-Ready)
- [x] **Lab 0:** Starter Foundry multi-turn text agent (`agents/poc1-starter`)
- [x] **Lab 1:** Realtime Foundry voice customer support agent (`agents/voice-support-agent`)
- [x] **Lab 2:** Finance Expenses Assistant agent client (`agents/expenses-agent`)
- [x] **Lab 3:** Text-to-Image POC agent client (`agents/text-to-image-agent`)
- [ ] **Lab 4 (Planned):** Azure Text Analytics / PII & Sentiment QA Agent (FastAPI-ready for Shipkit.ai)
- [ ] **Lab 5 (Planned):** RAG-Grounded AI-901 & Finance Policy Assistant powered by `study-notes/ai-901/` in Microsoft Foundry
