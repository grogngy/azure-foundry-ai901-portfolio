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

## 2. Python SDK Jargon: What Exactly Is an "Object"?

> **Key Clarification:** A **Python Object** is **NOT** a saved `.md` file, **NOT** a `.json` file on disk, and **NOT** the cloud API itself. It is a **live bundle in your computer's memory** while your Python script is running that holds **Data/Settings (properties)** + **Action Buttons (methods)** together.

### Object vs. Markdown File vs. JSON vs. API

| Term | What It Actually Is | Plain-English Analogy | Example |
| :--- | :--- | :--- | :--- |
| **`.md` File** | A saved text document on disk | A **notebook page** | `STUDY_PLAN.md` |
| **API** | The Azure cloud service listening at a URL | The **bank's call center** | `https://<resource>.services.ai.azure.com/` |
| **JSON Object (`{...}`)** | Structured `key: value` text sent over HTTPS | A **filled-out paper form** mailed to the API | `{"voice": "alloy", "format": "wav"}` |
| **Python Object** | A live in-memory bundle inside your running script | A **remote control** holding settings + buttons | `client = TextAnalyticsClient(...)`, `speech_config = SpeechConfig(...)` |

*(Why MeasureUp feels tricky: the exam uses **"object"** in TWO ways — a **Python object** in SDK code like `SpeechConfig`, and a **JSON object `{...}`** in REST API payloads like `audio: {"voice": "alloy", "format": "wav"}`!)*

### Seeing Python Objects Live in Real Code (Annotated)

**Example A — From Your Own Banking QA Lab (`agents/banking-qa-text-analyzer/app.py`):**
```python
# 1. CREATE A PYTHON OBJECT (the "remote control" in memory, NOT a file on disk)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# 2. PRESS AN ACTION BUTTON ("method") ON THAT OBJECT — notice the dot (.) and parentheses ()
pii_results = client.recognize_pii_entities(sample_tickets)

# 3. READ DATA ("properties") FROM THE RESULT OBJECT AZURE SENT BACK — dot (.) with NO parentheses
for pii in pii_results:
    print(pii.redacted_text)   # <-- Property (data stored inside the 'pii' result object)
    print(pii.is_error)        # <-- Property (True or False)
```

**Example B — From Your MeasureUp Speech SDK Questions:**
```python
# 1. CREATE THE 'SpeechConfig' OBJECT (a settings holder in memory)
speech_config = speechsdk.SpeechConfig(subscription=key, region=region)

# 2. SET PROPERTIES (settings) ON THAT OBJECT using a dot (.)
speech_config.speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"

# 3. CREATE A 'SpeechRecognizer' OBJECT and press its action button (method)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
speech_recognizer.start_continuous_recognition()   # <-- Method (action button with parentheses!)
```

### Quick 4-Piece Cheat Sheet

| Python Term | Plain-English Analogy | How to Spot It in Exam Code |
| :--- | :--- | :--- |
| **Library / SDK Package** | **Toolbox** you install once (`pip install`) | `from azure.ai.textanalytics import ...` |
| **Class / Client Object** | **Remote Control** created in memory | `client = TextAnalyticsClient(...)` |
| **Property / Attribute** | **Setting or Data Field** on the object | `object.setting` *(dot, NO `()`)* |
| **Method / Function** | **Action Button** on the object | `object.do_something()` *(dot + `()`)* |

### The `tkinter` ↔ Azure SDK Mental Map
Python's built-in desktop GUI library (`tkinter` — short for *Tk interface*, **not** on AI-901) uses the **exact same object pattern** as Azure AI SDKs:

| Concept | Built-in `tkinter` (Desktop Window) | Azure AI SDK (Cloud Client) |
| :--- | :--- | :--- |
| **Library** *(Toolbox)* | `import tkinter as tk` | `from azure.ai.projects import AIProjectClient` |
| **Class** *(Blueprint)* | `tk.Tk` / `tk.Button` | `AIProjectClient` / `TextAnalyticsClient` / `SpeechRecognizer` |
| **Object** *(Live instance in RAM)* | `window = tk.Tk()` | `client = TextAnalyticsClient(...)` |
| **Property** *(Setting/Data — no `()`)* | `window.title` | `response.output_text`, `speech_config.speech_synthesis_voice_name` |
| **Method** *(Action — has `()`)* | `window.mainloop()` | `openai_client.responses.create(...)`, `client.recognize_pii_entities(...)` |

### Direct Project Endpoint vs. Foundry Agent (When to Use Each)
* **Call a Foundry Agent (`agent_reference`)** when you want a **reusable assistant** managed centrally in Microsoft Foundry with saved instructions, tools, and stateful threads (`conversations.create()` → `responses.create()`).
* **Call the Project / Model directly (no Agent)** when your Python app needs **full code-level control** over custom prompt loops, model parameters, structured batch jobs, or stateless one-off calls (`chat.completions.create()`).

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
