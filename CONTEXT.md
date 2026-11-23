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
- **Target Exam Date:** **December 12, 2026** (using 1-year **MeasureUp** subscription; reschedulable if <78% on Dec 10 check)
- **Primary Weak Area Identified on MeasureUp:** Domain 2 (*Implement AI Solutions by Using Microsoft Foundry*) — specifically Python SDK jargon (objects, clients, methods), Foundry architecture, and **Azure Content Understanding Analyzers**.
- **Live GitHub Repo:** `https://github.com/grogngy/azure-foundry-ai901-portfolio`
- **Local Repo:** `c:\projects\azure-foundry-ai901-portfolio`
- **RAG-Structured Notes (9 total):** Indexed in `study-notes/KNOWLEDGE_INDEX.md` (including `04-text-analytics-sdk-lab.md` and `05-foundry-jargon-and-analyzers.md`).
- **Existing Foundry Agents Wired Up (All 4 share 1 Foundry Project Endpoint in local `.env`):**
  - `customer-support-agent-wcely` (Voice) → `agents/voice-support-agent/app.py`
  - `expenses-agent-wcely` (Text, multi-turn) → `agents/expenses-agent/app.py`
  - `text-to-image-poc-wcely` (Text / Multimodal, multi-turn) → `agents/text-to-image-agent/app.py`
  - `POC1` (Text, multi-turn) → `agents/poc1-starter/app.py`
- **Next Milestones:**
  1. Run a live local test of `agents/expenses-agent/app.py` (or `poc1-starter`) via `az login` + `.venv`.
  2. Complete **Domain 1** RAG study notes (Responsible AI, tokens/embeddings/RAG, AI workloads).
  3. Complete hands-on **Azure Text Analytics (`azure-ai-textanalytics`)** SDK lab and wrap our first Foundry agent in **FastAPI** for Shipkit.ai.
