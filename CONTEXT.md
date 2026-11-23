# Project Context & Portable Memory (`CONTEXT.md`)

> **Purpose:** Single source of truth shared between **Antigravity** (`GEMINI.md` + local repo) and **Gemini Gems** (web). Update this file after every study or build milestone so zero knowledge is lost across tools.

---

## Learner & Builder Profile
- **Name:** Wilson Cely (`grogngy`)
- **Background:** Business & Finance professional working in **Banking** and **IT Quality Assurance (IT QA)**.
- **Strengths:** Solid grasp of foundational AI theory, ML concepts, compliance, risk, and IT QA testing.
- **Target Growth Area:** Hands-on **Azure Python SDK** implementation, Git/GitHub workflow, and productionizing Foundry agents.
- **Preferred Style:** Baby steps, plain-English explanations before code, and real-world banking/finance/QA analogies.

## Goals & Target Architecture
1. **Certification:** Pass **Microsoft Exam AI-901 (Azure AI Fundamentals — Microsoft Foundry)**.
2. **RAG Knowledge Base:** Maintain all study notes in RAG-ready Markdown (YAML frontmatter + clean semantic sections) under `study-notes/ai-901/` for future grounding in Microsoft Foundry agents & Azure AI Search.
3. **Portfolio Architecture (Future SaaS Showcase):**
   - **Frontend:** Next.js via **Shipkit.ai** (Vercel / Azure App Service)
   - **Backend API:** Python (**FastAPI** / **Flask**)
   - **Database & Auth:** **Supabase**
   - **AI Layer:** **Microsoft Foundry** & Azure AI SDKs (`azure-ai-projects`, `openai`, `azure-ai-textanalytics`, `azure-ai-documentintelligence`)

## Current Status
- **Last Updated:** 2026-11-23
- **Target Exam Date:** **December 12, 2026** (using 1-year **MeasureUp** subscription; reschedulable if <78% on Dec 10 Go/No-Go check)
- **Primary Weak Area Identified on MeasureUp:** Domain 2 (*Implement AI Solutions by Using Microsoft Foundry*) — specifically Python SDK literacy (objects, clients, methods), Foundry architecture, Speech SDK, and **Azure Content Understanding Analyzers**.
- **Live GitHub Repo:** `https://github.com/grogngy/azure-foundry-ai901-portfolio`
- **Local Repo:** `c:\projects\azure-foundry-ai901-portfolio`
- **RAG-Structured Notes (10 notes + Practice Quiz Log):** Indexed in `study-notes/KNOWLEDGE_INDEX.md` (including `04-text-analytics-sdk-lab.md`, `05-foundry-jargon-and-analyzers.md`, `06-ai901-python-sdk-master-reference.md`, and `practice-quizzes.md`).
- **Hands-On Portfolio Apps Wired Up & Verified:**
  - `agents/banking-qa-text-analyzer/app.py` — Live-tested against Azure via passwordless `DefaultAzureCredential()`; hardened with chained fail-closed PII redaction (`recognize_pii_entities()` first) + automated `check_pii_leaks()` assertion.
  - 4 Microsoft Foundry Agents (all share 1 Foundry Project Endpoint in local gitignored `.env`, all syntax-verified):
    - `customer-support-agent-wcely` (Voice) → `agents/voice-support-agent/app.py`
    - `expenses-agent-wcely` (Text, multi-turn) → `agents/expenses-agent/app.py`
    - `text-to-image-poc-wcely` (Text / Multimodal, multi-turn) → `agents/text-to-image-agent/app.py`
    - `POC1` (Text, multi-turn `while` loop) → `agents/poc1-starter/app.py`

## Session Handoff (Pick Up Here Next Session)
- **Completed Today (2026-11-23):**
  - Built and live-tested the hardened Banking QA Text Analyzer lab (`azure-ai-textanalytics`).
  - Created `05-foundry-jargon-and-analyzers.md` (Foundry architecture, Python Object/`tkinter` mental map, direct Project vs. Agent calls, 4 Content Understanding Analyzer types) and `06-ai901-python-sdk-master-reference.md` (all 6 core AI-901 SDK libraries).
  - Decoded 4 MeasureUp exam traps in `practice-quizzes.md` (Audio Chat Completions, Long `.wav` Continuous Recognition, SSML `<voice>` override, Private Photo Vision Chat Completions).
  - Completed interactive SDK walkthrough & drills for **Libraries #1–#4** (`azure-identity`/`azure-core`, `azure-ai-projects` + `openai`, `azure-ai-textanalytics`, `azure-cognitiveservices-speech`).
- **Next Milestones (In Order — Keep AI-901 Focused):**
  1. **Resume SDK Walkthrough at Library #5 & #6:** Drill **#5 Azure Content Understanding** (`ContentUnderstandingClient`, `begin_analyze`, Base/RAG/Domain-Specific/Custom Analyzers) and **#6 Azure AI Vision** (`ImageAnalysisClient`, `analyze`/`analyze_from_url`, all 7 `VisualFeatures` enums).
  2. **Complete Domain 1 RAG Study Notes** under `study-notes/ai-901/01-ai-concepts/` (Responsible AI 6 pillars, tokens/embeddings/temperature/RAG grounding, AI workloads).
  3. **Run MeasureUp Study Mode & Certification Mode Drills** toward the **Dec 10 Go/No-Go gate** (85%+ = Go for Dec 12).
  4. *(Phase 2 — Deferred Until After AI-901)*: Wrap Foundry agents in **FastAPI** + Next.js (**Shipkit.ai**) + **Supabase**.
