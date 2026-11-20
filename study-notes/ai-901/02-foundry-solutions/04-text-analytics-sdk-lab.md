---
id: ai901-d2-04
title: "Azure AI Text Analytics Python SDK Lab (PII Redaction, Sentiment & Key Phrases)"
exam: AI-901
domain: "Domain 2: Implement AI Solutions Using Microsoft Foundry"
topics:
  - Azure AI Language SDK
  - PII Detection and Redaction
  - Sentiment Analysis
  - Key Phrase Extraction
  - Code Literacy for AI-901
keywords:
  - azure-ai-textanalytics
  - TextAnalyticsClient
  - AzureKeyCredential
  - DefaultAzureCredential
  - recognize_pii_entities
  - analyze_sentiment
  - extract_key_phrases
  - Responsible AI
  - banking QA
source: hands-on-lab
last_updated: 2026-11-20
---

# Azure AI Text Analytics Python SDK Lab

## 1. Overview & Exam Relevance
This lab implements the Microsoft Learn AI-901 unit **"Create a client application that analyzes text"** using a realistic **Banking & IT QA** scenario: triaging customer complaints while redacting Personally Identifiable Information (PII).

* **Portfolio Code:** `agents/banking-qa-text-analyzer/app.py`
* **SDK Package:** `azure-ai-textanalytics`

---

## 2. Core Capabilities Tested on AI-901
1. **PII Detection & Redaction (`recognize_pii_entities`):**
   * Identifies sensitive entities (Person, Email, PhoneNumber, BankAccountNumber, SSN) and returns a `redacted_text` version with asterisks (`****`).
   * *Responsible AI tie-in:* Directly supports the **Privacy & Security** principle before logging tickets or prompting an LLM.
2. **Sentiment Analysis (`analyze_sentiment`):**
   * Classifies text as `positive`, `neutral`, `negative`, or `mixed` with confidence scores (`confidence_scores.positive`, `.neutral`, `.negative`).
   * *Banking/QA tie-in:* Automatically routes negative fraud or billing disputes to high-priority QA review.
3. **Key Phrase Extraction (`extract_key_phrases`):**
   * Extracts the main talking points (e.g., `"duplicate wire transfer fee"`, `"daily transfer limits"`) for tagging and trend analysis.
4. **Language Detection (`detect_language`):**
   * Identifies the primary language and ISO code (e.g., `en`, `es`) for multilingual call centers.

---

## 3. Reading the Python SDK Pattern (3-Step Mental Model)
When reading any Azure AI Language snippet on AI-901, scan for three parts:
1. **Imports:** `TextAnalyticsClient` (from `azure.ai.textanalytics`) + a credential class (`AzureKeyCredential` or `DefaultAzureCredential`).
2. **Client Creation:** `client = TextAnalyticsClient(endpoint=endpoint, credential=credential)`
   * *Endpoint note:* Uses the **AI Services / Language root endpoint** (`https://<resource>.services.ai.azure.com/` or `https://<resource>.cognitiveservices.azure.com/`), NOT the `/api/projects/<project>` sub-path.
   * *RBAC note:* Passwordless `DefaultAzureCredential()` requires the **Cognitive Services User** role on the Azure resource; otherwise use `AzureKeyCredential(api_key)` from `.env`.
3. **Method Call & Loop:** Pass a Python `list` of strings (e.g., `client.analyze_sentiment(documents)`), loop through the results, check `if not doc.is_error`, and print the structured fields.
