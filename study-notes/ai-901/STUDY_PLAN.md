# Exam AI-901 Study Plan & Progress Tracker

- **Exam:** AI-901 — Microsoft Certified: Azure AI Fundamentals
- **Passing Score:** 700 / 1000
- **Expiration:** Fundamentals certifications do not expire
- **Target Exam Date:** *(TBD — update once scheduled)*

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

- [ ] **2.1 Microsoft Foundry Basics & Resource Setup**
  - Foundry portal navigation, projects, endpoints, Entra ID (`DefaultAzureCredential`) vs. API key auth
- [ ] **2.2 Model Catalog & Deployment**
  - Selecting, deploying, testing, and configuring foundational LLMs & multimodal models
- [ ] **2.3 Building Single-Agent Solutions**
  - Instructions, tools, knowledge grounding, conversation state, calling agents via Python SDK (`azure-ai-projects`)
- [ ] **2.4 Text, Speech, Vision & Information Extraction**
  - Lightweight multimodal apps, voice agents, image generation, and Azure Content Understanding
- [ ] **2.5 Reading Basic Python & REST/SDK Snippets**
  - Imports, environment variables, client initialization, sending prompts, parsing responses

---

## Hands-On Portfolio Milestones (Resume-Ready)
- [x] **Lab 0:** Starter Foundry text agent (`agents/poc1-starter`)
- [x] **Lab 1:** Realtime Foundry voice customer support agent (`agents/voice-support-agent`)
- [ ] **Lab 2 (Planned):** Finance / Banking QA Policy Assistant (RAG + Responsible AI guardrails)
- [ ] **Lab 3 (Planned):** Automated IT QA Test-Case & Requirement Reviewer Agent in Foundry
