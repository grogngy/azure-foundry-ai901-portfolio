---
id: ai901-d2-05
title: "AI-901 Plain-English Jargon Decoder: Foundry Architecture, Python Objects & Content Understanding Analyzers"
exam: AI-901
domain: "Domain 2: Implement AI Solutions Using Microsoft Foundry"
topics:
  - Microsoft Foundry Architecture
  - Python Objects Clients and Methods
  - Azure Content Understanding Analyzers
  - Prebuilt vs Custom Analyzers
keywords:
  - AI-901
  - analyzer
  - Azure Content Understanding
  - prebuilt-document
  - prebuilt-invoice
  - prebuilt-documentSearch
  - custom analyzer
  - field schema
  - AIProjectClient
  - TextAnalyticsClient
  - Python object
  - method
  - Foundry project
source: exam-prep-guide
last_updated: 2026-11-23
---

# AI-901 Plain-English Jargon Decoder (Domain 2)

> **Purpose:** Translates the technical Python, SDK, and Microsoft Foundry jargon from **MeasureUp** and **Exam AI-901** into plain-English banking/QA analogies.

---

## 1. Microsoft Foundry Architecture (The Building Analogy)

| Exam Term | Plain-English Banking Analogy | What It Does in Azure |
| :--- | :--- | :--- |
| **Microsoft Foundry Resource** | **The Bank Building** | Top-level Azure resource that owns billing, RBAC security, and the root AI Services endpoint (`https://<name>.services.ai.azure.com/`). |
| **Foundry Project** | **A Department Inside the Building** | Workspace (`.../api/projects/<project>`) that groups your deployed models, agents, evaluations, and files together. All agents in one project share one Project Endpoint. |
| **Model Deployment** | **A Specialist Brain on Call** | A deployed LLM or multimodal model (e.g., `gpt-4o`, `gpt-5-mini`) accessed via an endpoint. Stateless by itself. |
| **Foundry Agent** | **An Employee With a Job Description & Tools** | Combines a model + system instructions + conversation thread memory + tools (File Search / RAG, functions, grounding). |

---

## 2. Python SDK Jargon (Objects, Clients, Methods & Functions)

When MeasureUp shows a Python snippet, you do **not** need to memorize syntax—just recognize these 4 concepts:

| Python Term | Plain-English Analogy | Example You Already Built |
| :--- | :--- | :--- |
| **Library / SDK Package** | **Toolbox** you install once (`pip install`) | `azure-ai-projects`, `azure-ai-textanalytics` |
| **Class / Client Object** | **Remote Control** created from the toolbox, connected to your Azure endpoint + credentials | `client = AIProjectClient(endpoint, credential)` or `client = TextAnalyticsClient(endpoint, credential)` |
| **Method / Function** | **Action Button** on that remote control (always has parentheses `()`) | `client.analyze_sentiment(docs)`, `client.recognize_pii_entities(docs)`, `openai_client.responses.create(...)` |
| **Result Object / Properties** | **Filled-Out Report Form** returned by Azure; you read fields using a dot `.` | `response.output_text`, `pii.redacted_text`, `sentiment.confidence_scores.negative` |

---

## 3. What Is an "Analyzer"? (Azure Content Understanding)

> **Exam Trap Alert:** On **AI-901**, **"Analyzer"** refers specifically to **Azure Content Understanding** (multimodal information extraction in Microsoft Foundry), **not** Text Analytics!

* **Plain-English Definition:** An **Analyzer** is an automated **intake clerk with a checklist (field schema)**. You feed it unstructured content (**documents/PDFs, images, audio, or video**), and the analyzer combines AI models to extract structured **JSON fields** or **clean Markdown**.
* **What an Analyzer Defines:**
  1. **Modality (Input Type):** Document, image, audio, or video.
  2. **Extraction Schema:** Which fields, tables, transcripts, or key frames to pull out.
  3. **Output Format:** Structured JSON fields, Markdown, or RAG-ready chunks.

### The 4 Types of Analyzers Tested on AI-901
1. **Base Analyzers** — General-purpose starting points per modality:
   * `prebuilt-document`, `prebuilt-image`, `prebuilt-audio`, `prebuilt-video`
2. **RAG Analyzers** — Optimized to extract semantic, search-ready chunks for Retrieval-Augmented Generation:
   * `prebuilt-documentSearch`, `prebuilt-videoSearch`
3. **Domain-Specific Analyzers** — Ready-made industry templates:
   * `prebuilt-invoice`, `prebuilt-receipt`, `prebuilt-idDocument`
4. **Custom Analyzers** — Created by extending a Base Analyzer with your own **custom field schema** (e.g., extracting `LoanID`, `WireAmount`, and `ApprovalDate` from custom banking forms).

---

## 4. Quick Service-Matching Cheat Sheet (MeasureUp Shortcut)

When an exam question describes a scenario, match the clue to the service:

* **"Extract structured fields from PDFs, invoices, audio calls, or videos using an analyzer/schema"** → **Azure Content Understanding**
* **"Redact PII, detect sentiment, extract key phrases, or detect language in text"** → **Azure AI Language (`azure-ai-textanalytics`)**
* **"Convert speech to text, text to speech, or build a realtime voice assistant"** → **Azure AI Speech / Foundry Voice Agent**
* **"Create a stateful assistant with instructions, tools, and knowledge files"** → **Microsoft Foundry Agent Service (`azure-ai-projects`)**
* **"Authenticate without storing API keys in code"** → **Microsoft Entra ID (`DefaultAzureCredential` + Azure RBAC)**
