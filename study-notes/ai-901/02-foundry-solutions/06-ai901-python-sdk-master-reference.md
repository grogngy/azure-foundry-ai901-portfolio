---
id: ai901-d2-06
title: "AI-901 Master Python SDK Reference: All 6 Core Libraries, Client Objects & Methods"
exam: AI-901
domain: "Domain 2: Implement AI Solutions Using Microsoft Foundry"
topics:
  - Azure AI Projects SDK
  - OpenAI SDK
  - Azure AI Text Analytics SDK
  - Azure Speech SDK
  - Azure Content Understanding SDK
  - Azure AI Vision Image Analysis SDK
  - Azure Identity and Auth
keywords:
  - AIProjectClient
  - TextAnalyticsClient
  - SpeechConfig
  - SpeechRecognizer
  - SpeechSynthesizer
  - ContentUnderstandingClient
  - ImageAnalysisClient
  - VisualFeatures
  - DefaultAzureCredential
  - AzureKeyCredential
  - begin_analyze
  - start_continuous_recognition
  - speak_ssml_async
source: master-exam-reference
last_updated: 2026-11-23
---

# AI-901 Master Python SDK Reference (All 6 Core Libraries)

> **Exam Superpower:** Almost every Python question on **Exam AI-901** comes from these **6 core libraries**. You do **not** need to memorize syntax—just match **Library → Client Object → Key Method → Exam Trap**.

---

## Quick Status Matrix (What's Already in Your `.venv` & Repo)

| # | AI Workload | Python Library (`pip`) | Main Client Object(s) | In Your `.venv`? |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Auth (All Services)** | `azure-identity` / `azure-core` | `DefaultAzureCredential`, `AzureKeyCredential` | **Yes** (`1.27.0` / `1.41.0`) |
| **2** | **Foundry Agents & GenAI** | `azure-ai-projects` + `openai` | `AIProjectClient`, `OpenAI` / `AzureOpenAI` | **Yes** (`2.11.0` / `3.57.0`) |
| **3** | **NLP / Text Analysis** | `azure-ai-textanalytics` | `TextAnalyticsClient` | **Yes** (`5.4.0`) |
| **4** | **Speech (STT / TTS / SSML)** | `azure-cognitiveservices-speech` | `SpeechConfig`, `AudioConfig`, `SpeechRecognizer`, `SpeechSynthesizer` | Not yet (conceptual + MeasureUp) |
| **5** | **Multimodal Extraction (Analyzers)** | `azure-ai-contentunderstanding` | `ContentUnderstandingClient` | Not yet (Priority Week 1) |
| **6** | **Computer Vision (Images & OCR)** | `azure-ai-vision-imageanalysis` | `ImageAnalysisClient` (+ `VisualFeatures`) | Not yet (Week 2) |

---

## 1. Authentication (`azure-identity` & `azure-core`)
* **Client/Credential Objects:**
  * **`DefaultAzureCredential()`** — Passwordless Microsoft Entra ID auth (uses `az login` locally or Managed Identity in Azure). **Enterprise best practice** (requires Azure RBAC roles like *Cognitive Services User*).
  * **`AzureKeyCredential(api_key)`** — Authenticates with a static subscription/API key stored in `.env`.
* **Exam Trap:** Never hardcode keys in `.py` files; prefer `DefaultAzureCredential` + RBAC when a question asks for **passwordless / keyless / Entra ID / least-privilege** authentication.

---

## 2. Microsoft Foundry & Generative AI (`azure-ai-projects` + `openai`)
* **Main Client Objects:**
  * `AIProjectClient(endpoint=project_endpoint, credential=...)` — Connects to your **Foundry Project** (`.../api/projects/<name>`).
  * `openai_client = project_client.get_openai_client(...)` — Bound OpenAI client for models & Foundry Agents.
* **Key Methods:**
  * `openai_client.conversations.create()` → Starts a **stateful** multi-turn thread.
  * `openai_client.responses.create(conversation=..., input=...)` → Sends a turn to a Foundry Agent; read `response.output_text`.
  * `client.chat.completions.create(model=..., messages=..., modalities=..., audio=...)` → Standard Chat Completions call.
* **Classic AI-901 Traps:**
  * **Audio + Text on Chat Completions:** Must add `"audio"` to `modalities=["text", "audio"]` **AND** pass `audio={"voice": "...", "format": "wav"}`.
  * **`session.update`** belongs to the **Realtime WebSocket API**, NOT standard Chat Completions.
  * **Project Endpoint** (`/api/projects/...`) is for `AIProjectClient` & Agents; **Azure OpenAI / AI Services root endpoint** is for direct model/NLP calls.

---

## 3. Azure AI Language / NLP (`azure-ai-textanalytics`)
* **Main Client Object (only 1!):** `TextAnalyticsClient(endpoint, credential)`
* **Category A — Instant Prebuilt Methods (6):**
  * `detect_language()` — Language + ISO code (`en`, `es`).
  * `analyze_sentiment()` — Positive / Neutral / Negative / Mixed + confidence scores + opinion mining.
  * `extract_key_phrases()` — Core talking points.
  * `recognize_entities()` — General NER (people, orgs, dates, money, locations).
  * `recognize_pii_entities()` — Detects & masks sensitive personal info (`redacted_text`).
  * `recognize_linked_entities()` — Links well-known entities to **Wikipedia URLs**.
* **Category B — Long-Running `begin_...` Methods (7 — return a poller → call `.result()`):**
  * `begin_extract_summary()` (**Extractive** — verbatim key sentences) vs. `begin_abstract_summary()` (**Abstractive** — paraphrased summary).
  * `begin_single_label_classify()` (1 custom label) vs. `begin_multi_label_classify()` (multiple custom labels).
  * `begin_recognize_custom_entities()` (custom domain entities).
  * `begin_analyze_healthcare_entities()` (clinical/medical NLP).
  * `begin_analyze_actions()` (runs multiple NLP tasks in one batch).
* **Banking QA Trap:** Always run `recognize_pii_entities()` **first** and feed `redacted_text` into downstream calls so PII doesn't leak!

---

## 4. Azure AI Speech (`azure-cognitiveservices-speech` — imported as `speechsdk`)
* **Config Objects (Settings Holders):**
  * `speechsdk.SpeechConfig(subscription=key, region=region)` — Holds auth, language (`speech_recognition_language`), and voice (`speech_synthesis_voice_name`).
  * `speechsdk.AudioConfig(filename="meeting1.wav")` or `use_default_microphone=True` — Tells Azure where audio comes from or goes to.
* **Action Client Objects & Key Methods:**
  * **`SpeechRecognizer(speech_config, audio_config)`** *(Speech → Text)*:
    * `recognize_once_async().get()` → **Single short utterance ONLY** (stops at first pause / ~15–30s!).
    * `start_continuous_recognition()` + **`.recognized`** event → **Full multi-minute recordings** (`meeting1.wav`).
  * **`SpeechSynthesizer(speech_config, audio_config)`** *(Text → Speech)*:
    * `speak_text_async(text)` → Uses `SpeechConfig` voice settings.
    * `speak_ssml_async(ssml)` → Uses XML SSML script (**`<voice name="...">` inside SSML overrides `SpeechConfig`!**).
  * **`TranslationRecognizer`** *(Speech Translation)* — Translates spoken audio directly into target text/audio languages.
* **Classic AI-901 Traps:**
  * **`recognizing`** (`-ing` = noisy partial draft) vs. **`recognized`** (`-ed` = final completed sentence).
  * **SSML `<voice>` ALWAYS overrides `SpeechConfig`** (`speech_synthesis_voice_name` & `speech_synthesis_language`).
  * **`endpoint_id`** is only needed for **Custom Neural Voices**, not standard prebuilt voices.

---

## 5. Azure Content Understanding (`azure-ai-contentunderstanding`)
* **Main Client Object:** `ContentUnderstandingClient(endpoint, credential)`
* **Key Method (Long-Running Poller):**
  * `poller = client.begin_analyze(analyzer_id="...", inputs=[AnalyzeInput(url=...)])`
  * `result = poller.result()`
* **Key Concept — The 4 Analyzer Types:**
  1. **Base:** `prebuilt-document`, `prebuilt-image`, `prebuilt-audio`, `prebuilt-video`
  2. **RAG:** `prebuilt-documentSearch`, `prebuilt-videoSearch`
  3. **Domain-Specific:** `prebuilt-invoice`, `prebuilt-receipt`, `prebuilt-idDocument`
  4. **Custom:** Extends a Base analyzer with your own **field schema** (e.g., extracting banking fields into JSON/Markdown).
* **Exam Trap:** Look for **"multimodal extraction"**, **"analyzer"**, or **"field schema"** (documents + images + audio + video → structured JSON/Markdown) → **Content Understanding**! *(Older/document-only form extraction questions may also mention `azure-ai-documentintelligence` / `DocumentIntelligenceClient`.)*

---

## 6. Azure AI Vision — Image Analysis (`azure-ai-vision-imageanalysis`)
* **Main Client Object:** `ImageAnalysisClient(endpoint, credential)`
* **Key Methods:**
  * `client.analyze_from_url(image_url=..., visual_features=[...])` — Analyzes an image at a URL.
  * `client.analyze(image_data=..., visual_features=[...])` — Analyzes raw local image bytes.
* **Key Enum (`VisualFeatures` — Pass a list of what you want Azure to detect):**
  * `VisualFeatures.CAPTION` — One sentence describing the whole image (`result.caption.text`).
  * `VisualFeatures.DENSE_CAPTIONS` — Captions for up to 10 sub-regions of the image.
  * `VisualFeatures.TAGS` — Keywords describing scenery, objects, and actions (`result.tags.values`).
  * `VisualFeatures.OBJECTS` — Physical objects **with bounding box coordinates**.
  * `VisualFeatures.PEOPLE` — Detects people **with bounding box coordinates**.
  * `VisualFeatures.READ` — **OCR** (extracts printed or handwritten text: `result.read.blocks` → `lines`).
  * `VisualFeatures.SMART_CROPS` — Thumbnail crop regions for target aspect ratios.
* **Classic AI-901 Traps:**
  * Need **OCR / text inside an image**? Pick **`VisualFeatures.READ`**.
  * Need **where an object is located (bounding box)**? Pick **`OBJECTS`** (not `TAGS`, which only returns keyword labels without coordinates!).
  * Need **descriptions of multiple regions**? Pick **`DENSE_CAPTIONS`** (not `CAPTION`).
