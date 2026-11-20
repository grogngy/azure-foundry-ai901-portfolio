---
id: ai901-fnd-01
title: "Azure AI Certification & Portfolio Architecture Roadmap"
exam: AI-901
domain: "Cross-Domain (Architecture & Portfolio)"
topics:
  - Full-Stack AI Architecture
  - Shipkit.ai
  - Azure AI Python SDKs
  - Antigravity Workspace Rules
keywords:
  - AI-901
  - Microsoft Foundry
  - Shipkit.ai
  - Next.js
  - FastAPI
  - Supabase
  - azure-ai-projects
  - azure-ai-textanalytics
  - azure-ai-documentintelligence
  - GEMINI.md
source: gemini-web-import
last_updated: 2026-11-20
---

# Azure AI Certification & Portfolio Architecture Roadmap

## 1. Core Objectives
* **Primary Goal:** Pass the Microsoft Azure AI Fundamentals certification (`AI-901`) while mastering production-ready AI engineering concepts.
* **Portfolio Strategy:** Build a modular, full-stack SaaS web application using an existing **Shipkit.ai** boilerplate. The portfolio homepage will showcase multiple independent AI agents/tools built throughout the certification journey.

---

## 2. Production Full-Stack Architecture
Rather than building standalone command-line scripts, all Python exercises and Azure SDK integrations are framed as backend engines powering a real-world SaaS product:

* **Frontend & Web Framework:** Next.js (via **Shipkit.ai**), hosted on **Vercel** (or Azure App Service).
* **Backend API Layer:** Python (**FastAPI** or **Flask**) acting as the bridge between the user interface and cloud AI services.
* **Database & Auth:** **Supabase** (leveraging existing Shipkit.ai integrations).
* **AI & Cloud Services:** **Microsoft Foundry** & **Azure AI Services**, accessed programmatically via official SDKs.

---

## 3. Development Environment & Workspace Rules
* **Primary IDE:** **Google Antigravity** (authenticated via existing Google AI subscription, avoiding extra Copilot token costs).
* **Project Directory Hygiene:**
  * Keep all source code (`.py` files), `.env` configuration files, and Markdown documentation in the **main project root** (outside the virtual environment).
  * Keep all installed dependencies isolated strictly inside the local virtual environment folder (`.venv/`).
* **Persistent Agent Memory (`GEMINI.md`):**
  * Instead of maintaining a separate browser-based Gemini Gem with manual Google Drive syncing, store persistent mentor instructions and project rules in a root `GEMINI.md` file (and modular `.agents/rules/` files) so Antigravity reads them natively on every turn.
  * *Optional Mobile Extension:* Copy `GEMINI.md` into a Gemini Gem later only if mobile/away-from-desk quizzing is desired.

---

## 4. SDK & Library Fundamentals
* **What an SDK Is:** A Software Development Kit is a collection of pre-built, language-specific client libraries provided by cloud vendors (e.g., Microsoft Azure) to abstract REST API calls, authentication, and data serialization.
* **IDE & OS Agnostic:** Python SDKs run identically inside Google Antigravity's terminal and `.venv`—no Firebase lock-in is required.
* **Key Azure AI Python Packages:**
  * `openai` / `azure-ai-projects`: Direct interface to large language models (GPT) and Microsoft Foundry project endpoints for generative AI, chat, and reasoning.
  * `azure-ai-textanalytics`: Specialized Natural Language Processing (NLP) tasks such as sentiment analysis, language detection, key phrase extraction, and PII redaction.
  * `azure-ai-documentintelligence`: Automated extraction of structured key-value pairs and tables from forms, receipts, and PDFs.
* **Multi-Language Ecosystem:** While Python is the primary focus for AI/ML, Microsoft provides official SDK parity for **.NET (C#)**, **Java**, and **JavaScript/TypeScript (Node.js)**.

---

## 5. Immediate Next Steps
1. **Initialize Antigravity Workspace:** Open the local project folder in Google Antigravity, confirm `.venv` activation, and save this file as `00-study-roadmap.md` (alongside a `GEMINI.md` instruction file).
2. **Microsoft Foundry & OpenAI SDK Lab:** Examine how the `openai` and `azure-ai-projects` Python libraries authenticate (Entra ID / API keys via `.env`) and connect to a deployed model endpoint in Microsoft Foundry.
3. **Build First Portfolio Agent:** Wrap the first working Azure OpenAI / Text Analytics Python module into a clean API endpoint ready for integration into Shipkit.ai.
