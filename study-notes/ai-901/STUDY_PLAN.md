# Exam AI-901 Study Plan & 19-Day Action Roadmap (Nov 23 – Dec 12)

- **Exam:** AI-901 — Microsoft Certified: Azure AI Fundamentals
- **Scheduled Exam Date:** **December 12, 2026** *(reschedulable if needed)*
- **Practice Platform:** **MeasureUp** (1-year subscription — Study Mode + Certification Mode)
- **Official Microsoft Learn Course:** [Course AI-901T00-A: Introduction to AI in Azure](https://learn.microsoft.com/training/courses/ai-901t00)
- **Official Exam & Study Guide Page:** [Exam AI-901 Certification Page](https://learn.microsoft.com/credentials/certifications/exams/ai-901/)
- **RAG Knowledge Index:** [../KNOWLEDGE_INDEX.md](../KNOWLEDGE_INDEX.md)

---

## 19-Day Targeted Action Plan (Fixing Domain 2 Weaknesses First)

> **Rule of Thumb:** Do **not** study randomly. Every session follows 3 steps: **(1) Read 1 plain-English module/note → (2) Decode 1 short Python snippet together → (3) Drill 10–15 MeasureUp Study Mode questions on that exact topic and log every missed term.**

### Week 1 (Nov 23 – Nov 29): Decode Foundry Architecture, SDK Jargon & Analyzers
* **Step 1 — Days 1–2 (Nov 23–24): Jargon & Architecture Reset (START HERE)**
  - Read [05-foundry-jargon-and-analyzers.md](02-foundry-solutions/05-foundry-jargon-and-analyzers.md) (Foundry Resource vs. Project, Python Objects/Clients/Methods, and Analyzers).
  - Review official Microsoft Learn module: *Introduction to Microsoft Foundry* inside [AI-901T00](https://learn.microsoft.com/training/courses/ai-901t00).
  - **Goal:** Never get tripped up by "project", "endpoint", "client object", "method", or "analyzer" again.
* **Step 2 — Days 3–4 (Nov 25–26): Azure Content Understanding & Information Extraction**
  - Learn the 4 **Analyzer** types (`Base`, `RAG`, `Domain-Specific`, `Custom`) and field schemas.
  - Review Microsoft Learn unit on **Information Extraction / Content Understanding**.
  - Drill 15 MeasureUp questions specifically on **Content Understanding & Extraction**.
* **Step 3 — Days 5–7 (Nov 27–29): Foundry Agents, Models & Python SDK Literacy**
  - Walk line-by-line through your own [agents/expenses-agent/app.py](../../agents/expenses-agent/app.py) and [agents/banking-qa-text-analyzer/app.py](../../agents/banking-qa-text-analyzer/app.py).
  - Practice identifying the 3 exam snippet clues: **Import → Auth (`DefaultAzureCredential` vs. `AzureKeyCredential`) → Method Call**.
  - Review Microsoft Learn modules on **Generative AI apps & Single-Agent Solutions in Microsoft Foundry**.

### Week 2 (Nov 30 – Dec 6): Speech, Vision, NLP & Domain 1 Polish
* **Step 4 — Days 8–9 (Nov 30–Dec 1): Speech & Computer Vision Workloads**
  - Speech-to-Text, Text-to-Speech, Speech Translation, and Vision/Multimodal image analysis & generation.
  - Drill MeasureUp questions on Speech & Vision.
* **Step 5 — Days 10–11 (Dec 2–3): Domain 1 Lock-In (40–45% of Exam)**
  - Build & review RAG notes in `01-ai-concepts/`: Responsible AI (6 principles), tokens, context windows, temperature/top-p, embeddings, and RAG grounding.
* **Step 6 — Days 12–14 (Dec 4–6): First Full MeasureUp Diagnostic + Mistake Log**
  - Take 1 full MeasureUp **Study Mode** test.
  - Paste every missed/confusing question topic into Antigravity → we turn every weakness into a plain-English flashcard in [practice-quizzes.md](practice-quizzes.md).

### Week 3 (Dec 7 – Dec 12): Certification Mode Readiness & Go/No-Go Check
* **Step 7 — Days 15–17 (Dec 7–9): Targeted Remediation + Certification Mode #1**
  - Drill ONLY your weakest Domain 2 sub-topics in MeasureUp.
  - Take **MeasureUp Certification Mode #1** (target **80%+**).
* **Step 8 — Days 18–19 (Dec 10–11): Final Readiness Gate (Go / Reschedule Decision)**
  - Take **MeasureUp Certification Mode #2**.
  - **Go Decision:** Scoring **85%+** consistently → take **AI-901 on Dec 12** with total confidence!
  - **Reschedule Decision:** Scoring **<78%** on Dec 10 → reschedule by 7–10 days stress-free using your MeasureUp subscription.

---

## Domain Checklist Tracker

### Foundations & Architecture
- [x] Full-stack portfolio roadmap (saved for post-AI-901 / AI-102)
- [x] Python virtual environments (`.venv`) & REST API / JSON basics
- [x] Plain-English Jargon Decoder & Analyzers guide ([05-foundry-jargon-and-analyzers.md](02-foundry-solutions/05-foundry-jargon-and-analyzers.md))

### Domain 1: Identify AI Concepts and Capabilities (40–45%)
- [ ] **1.1 Responsible AI Principles** (Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, Accountability)
- [ ] **1.2 Core Model Concepts** (Tokens, context windows, prompts, embeddings, temperature/top-p, RAG)
- [ ] **1.3 AI Workloads** (Generative AI, Agentic AI, NLP, Speech, Computer Vision, Information Extraction)

### Domain 2: Implement AI Solutions Using Microsoft Foundry (55–60%)
- [x] **2.1 Foundry Architecture, Endpoints & Azure RBAC**
- [x] **2.2 Single-Agent Solutions** (`poc1-starter`, `expenses-agent`, `text-to-image-agent`, `voice-support-agent`)
- [x] **2.3 Text Analytics SDK Lab** (`banking-qa-text-analyzer` — chained PII redaction, sentiment, key phrases)
- [x] **2.4 Azure Content Understanding & Analyzers** *(4 analyzer types, 3-switch rule, REST `202` polling & typed JSON paths logged in `practice-quizzes.md`)*
- [ ] **2.5 Model Catalog, Deployment & Vision SDK Literacy** *(Library #6 `ImageAnalysisClient` + 7 `VisualFeatures` next)*
