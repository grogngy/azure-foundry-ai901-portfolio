---
id: ai901-kb-index
title: "AI-901 & Microsoft Foundry RAG Knowledge Index"
exam: AI-901
domain: "Master Index"
topics:
  - RAG Grounding Standards
  - Knowledge Base Manifest
  - Executive Synthesis
keywords:
  - RAG
  - grounding
  - Azure AI Search
  - Microsoft Foundry
  - AI-901
  - knowledge base
source: curated-index
last_updated: 2026-11-20
---

# AI-901 & Microsoft Foundry RAG Knowledge Index

> **Purpose:** This knowledge base is structured for **both human study and Retrieval-Augmented Generation (RAG) / agent grounding** in Microsoft Foundry, Azure AI Search, and Gemini Gems.

---

## RAG Grounding Standards Used Across All Notes
Every study document under `study-notes/ai-901/` follows four RAG-readiness conventions:
1. **YAML Frontmatter Metadata:** Consistent `id`, `title`, `exam`, `domain`, `topics`, `keywords`, `source`, and `last_updated` fields for accurate metadata filtering and hybrid search.
2. **Semantic Chunk Boundaries:** Clean `##` (H2) headings with self-contained sections so Markdown splitters create coherent embeddings.
3. **Zero Duplicate Files:** Each topic lives in exactly one canonical path so vector indexes never retrieve stale or duplicated chunks.
4. **Zero Secrets:** Endpoints, subscription IDs, and API keys are strictly kept out of Markdown notes (stored only in gitignored `.env`).

---

## Knowledge Base Manifest (7 Imported Notes Organized)

| ID | Title | Domain | File |
| :--- | :--- | :--- | :--- |
| `ai901-fnd-01` | Azure AI Certification & Portfolio Architecture Roadmap | Cross-Domain (Architecture) | [01-portfolio-architecture-roadmap.md](ai-901/00-foundations-and-roadmap/01-portfolio-architecture-roadmap.md) |
| `ai901-fnd-02` | AI-901 Python & SDK Study Plan | Domain 2 (Python SDK) | [02-python-sdk-study-plan.md](ai-901/00-foundations-and-roadmap/02-python-sdk-study-plan.md) |
| `ai901-fnd-03` | Azure AI Fundamentals & Python Virtual Environments | Cross-Domain (Dev Foundations) | [03-python-virtual-environments.md](ai-901/00-foundations-and-roadmap/03-python-virtual-environments.md) |
| `ai901-fnd-04` | Voice-Agent SaaS & REST API Architecture | Domain 1 & 2 (Speech & REST) | [04-rest-apis-and-voice-agent-saas.md](ai-901/00-foundations-and-roadmap/04-rest-apis-and-voice-agent-saas.md) |
| `ai901-d2-01` | Azure AI Foundry & VS Code Setup Summary | Domain 2 (Foundry Setup) | [01-foundry-quickstart-and-vscode.md](ai-901/02-foundry-solutions/01-foundry-quickstart-and-vscode.md) |
| `ai901-d2-02` | Foundry POC: Endpoints, Models vs. Agents & Multi-Turn State | Domain 2 (Foundry Agents) | [02-foundry-poc-models-vs-agents.md](ai-901/02-foundry-solutions/02-foundry-poc-models-vs-agents.md) |
| `ai901-d2-03` | Azure RBAC & Foundry Resource Permissions | Domain 2 (Security & RBAC) | [03-azure-rbac-and-foundry-access.md](ai-901/02-foundry-solutions/03-azure-rbac-and-foundry-access.md) |

---

## Executive Synthesis (Key Takeaways Captured So Far)

### 1. Target Full-Stack SaaS Portfolio Architecture
* **Frontend:** Next.js via **Shipkit.ai** (Vercel or Azure App Service)
* **Backend API Bridge:** Python (**FastAPI** or **Flask**) wrapping Azure AI SDK modules
* **Database & Auth:** **Supabase**
* **AI Layer:** **Microsoft Foundry** & Azure AI Services (`azure-ai-projects`, `openai`, `azure-ai-textanalytics`, `azure-ai-documentintelligence`)

### 2. Core Microsoft Foundry & Azure Concepts Covered
* **Project Endpoint vs. Azure OpenAI Endpoint:** Use `FOUNDRY_PROJECT_ENDPOINT` for managing projects, agents, and conversation threads; use the Azure OpenAI endpoint for direct standalone model calls.
* **Stateless Models vs. Stateful Agents:** Direct model calls are single-turn/stateless; Foundry Agents retain instructions, personas, and multi-turn history via `conversations.create()` + `responses.create(conversation=conversation.id, ...)`.
* **Security & Governance (Azure RBAC):** Least-privilege role assignments at subscription, resource group, or workspace scope govern access to Foundry IQ, AI Solution Templates, Chat Completion Models, and Dev Packs.
* **REST APIs & Voice SaaS:** Clients send HTTPS requests with auth headers (`API key` / Entra ID token) and a `JSON` body to a REST endpoint; voice-agent SaaS combines Azure Speech + semantic turn detection for call centers, airlines, healthcare, and hospitality.
* **Dev Hygiene:** Short paths (`C:\projects`), isolated `.venv` per POC managed via terminal, secrets strictly in `.env`.

### 3. Next Knowledge Gaps to Fill for AI-901
* **Domain 1 (40–45%):** Responsible AI principles (6 pillars), tokens/embeddings/temperature/RAG grounding, vision/NLP/extraction workload comparison.
* **Domain 2 (55–60%):** Hands-on `azure-ai-textanalytics` lab (*"Create a client application that analyzes text"*), Content Understanding / Document Intelligence, and multi-turn `while` loop upgrade for `POC1`.
