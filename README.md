# Microsoft Foundry AI Agent Portfolio & AI-901 Study Hub

> **Focus:** Practical AI agent development, RAG knowledge engineering, Responsible AI governance, and quality assurance on **Microsoft Azure AI Foundry** — combining Banking, Finance, and IT QA experience with hands-on generative & agentic AI engineering.

---

## Certification & RAG Knowledge Base
- **Target Exam:** **AI-901 — Microsoft Certified: Azure AI Fundamentals**
- **Master RAG Knowledge Index:** [study-notes/KNOWLEDGE_INDEX.md](study-notes/KNOWLEDGE_INDEX.md) *(structured with YAML frontmatter & clean semantic sections for Microsoft Foundry / Azure AI Search grounding)*
- **Study Plan & Progress Tracker:** [study-notes/ai-901/STUDY_PLAN.md](study-notes/ai-901/STUDY_PLAN.md)
- **Exam Focus Areas:**
  1. Identify AI concepts and capabilities (40–45%)
  2. Implement AI solutions using Microsoft Foundry (55–60%)

---

## Agent Portfolio (Microsoft Foundry)

| Project | Description | Capabilities | Folder |
| :--- | :--- | :--- | :--- |
| **POC1 Starter Agent** | Conversational agent using the Microsoft Foundry Projects SDK & Responses API with Entra ID auth. | Text responses, conversation state, `DefaultAzureCredential` | [agents/poc1-starter](agents/poc1-starter/) |
| **Realtime Voice Support Agent** | Hands-free bidirectional audio customer support agent with live barge-in support. | Realtime voice streaming (PCM16), live transcripts, barge-in | [agents/voice-support-agent](agents/voice-support-agent/) |

*(Roadmap: Wrap Foundry & Azure AI Python agents in FastAPI endpoints to power a modular **Shipkit.ai / Next.js + Supabase** web portfolio.)*

---

## Repository Structure

```text
azure-foundry-ai901-portfolio/
├── README.md                              # Portfolio overview & project showcase
├── GEMINI.md                              # Native persistent Antigravity workspace instructions
├── CONTEXT.md                             # Portable project & study memory log
├── .env.example                           # Safe environment variable template
├── gem-instructions/                      # Optional system prompt for mobile Gemini Gem
├── imports/                               # Staging folder for importing new notes
├── study-notes/
│   ├── KNOWLEDGE_INDEX.md                 # Master RAG manifest & executive summary
│   └── ai-901/
│       ├── STUDY_PLAN.md                  # Domain-by-domain AI-901 tracker
│       ├── 00-foundations-and-roadmap/    # Architecture, Python SDK plan, venv, REST APIs
│       ├── 01-ai-concepts/                # Domain 1 notes
│       ├── 02-foundry-solutions/          # Domain 2 notes (Foundry setup, POC, RBAC)
│       └── practice-quizzes.md            # Practice questions & review log
└── agents/
    ├── poc1-starter/                      # Starter Foundry agent client
    └── voice-support-agent/               # Realtime Foundry voice agent client
```

---

## Quick Start (Local Development)

1. **Authenticate with Azure CLI:**
   ```powershell
   az login
   ```
2. **Configure environment variables:**
   Copy `.env.example` to `.env` and set your Microsoft Foundry project endpoint and agent names.
3. **Run a sample agent:**
   See each project's `README.md` inside `agents/` for package requirements and run commands.
