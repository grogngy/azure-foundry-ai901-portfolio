# Banking QA Ticket Triage & PII Redactor (`azure-ai-textanalytics`)

A compact, recruiter-ready **AI-901 Python SDK Proof of Concept** directly aligned with the Microsoft Learn module **`Get started with text analysis in Azure`** — applied to a real **Banking & IT QA** workflow.

## Real-World Banking & QA Use Case
Before storing customer support tickets in QA dashboards or forwarding them to an LLM, financial teams must protect customer privacy and prioritize urgent complaints. This 100-line Python lab demonstrates three Azure AI Language capabilities in one pass:
1. **PII Detection & Redaction (`recognize_pii_entities`):** Automatically masks names, emails, phone numbers, and account numbers *(Responsible AI — Privacy & Security)*.
2. **Sentiment Analysis (`analyze_sentiment`):** Flags negative complaints for immediate QA escalation.
3. **Key Phrase Extraction (`extract_key_phrases`):** Extracts core complaint topics (`duplicate wire transfer fee`, `online banking PIN`) for automated QA categorization.

---

## AI-901 Python Code Literacy Cheat Sheet
Every `azure-ai-textanalytics` snippet on **Exam AI-901** follows these 3 building blocks:

| Code Pattern | Plain-English Meaning |
| :--- | :--- |
| `from azure.ai.textanalytics import TextAnalyticsClient` | Imports the Azure AI Language SDK client class. |
| `AzureKeyCredential(key)` or `DefaultAzureCredential()` | Proves your identity using either an API key or passwordless Entra ID (`az login`). |
| `client.analyze_sentiment(docs)` / `recognize_pii_entities(docs)` / `extract_key_phrases(docs)` | Sends a Python list of text strings as JSON over HTTPS and returns structured results. |

---

## How to Run Locally
1. Install the SDK inside your `.venv`:
   ```powershell
   c:\projects\.venv\Scripts\pip.exe install azure-ai-textanalytics
   ```
2. Verify `.env` contains `AZURE_LANGUAGE_ENDPOINT` (your Azure AI Services / Foundry resource root URL) and either `az login` (with **Cognitive Services User** RBAC role) or `AZURE_LANGUAGE_KEY`.
3. Run the lab:
   ```powershell
   c:\projects\.venv\Scripts\python.exe agents/banking-qa-text-analyzer/app.py
   ```
