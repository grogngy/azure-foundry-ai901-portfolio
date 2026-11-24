---
id: ai901-quiz-log
title: "AI-901 MeasureUp Practice Quizzes & Decoded Flashcards"
exam: AI-901
domain: "Domain 2: Implement AI Solutions Using Microsoft Foundry"
topics:
  - MeasureUp Error Log
  - Audio Chat Completions
  - Azure Speech SDK Continuous Recognition
  - FileSearchTool Citations and Run Steps
  - OpenTelemetry Agent Tracing
  - Entra ID TokenCredential and Custom Subdomains
  - Azure Content Understanding Analyzers and Typed JSON
keywords:
  - modalities
  - audio object
  - session.update
  - recognize_once_async
  - start_continuous_recognition
  - recognized vs recognizing
  - SpeechConfig
  - FileSearchTool
  - RunAdditionalFieldList.FILE_SEARCH_CONTENTS
  - OpenTelemetry
  - execute_tool
  - tool.call.arguments
  - TokenCredential
  - custom subdomain
  - HTTP 401 vs 403
  - returnDetails
  - enableSegment
  - cameraShotTimesMs
  - valueObject
  - valueNumber
source: measureup-study-log
last_updated: 2026-11-24
---

# AI-901 Practice Quizzes & Review Log

Track practice questions, decoded jargon, and exam traps here so every missed or tricky MeasureUp question turns into permanent RAG study memory.

## Session Log
| Date | Source | Topic | Outcome | Key Takeaway |
| :--- | :--- | :--- | :--- | :--- |
| 2026-11-23 | MeasureUp | Audio-enabled Chat Completions (`modalities` + `audio` object) | Correct | Add `"audio"` to `modalities` array AND set `voice` + `format` in `audio` object. |
| 2026-11-23 | MeasureUp | Azure Speech SDK — Long Audio Transcription (`meeting1.wav`) | Missed → Decoded | Use `start_continuous_recognition()` + `recognized` event (not `recognize_once_async()`). |
| 2026-11-23 | MeasureUp | Azure Speech SDK — SSML `<voice>` Overrides `SpeechConfig` | Missed → Decoded | `speak_ssml_async()` uses the `<voice name="...">` inside the SSML document and ignores `SpeechConfig` voice/language settings. |
| 2026-11-23 | MeasureUp | Vision Chat Completions — Answering Questions About Private Uploaded Photos | Partial → Decoded | Call `chat/completions` on vision-enabled chat model AND attach photo as an `image_url` content part (using a base64 `data:image/...` URI for private files). |
| 2026-11-23 | SDK Walkthrough (#2) | Foundry Stateful Threads (`conversations.create()`) | Correct | `openai_client.conversations.create()` starts a stateful multi-turn thread; pass `conversation.id` to `responses.create()`. |
| 2026-11-23 | SDK Walkthrough (#3) | `TextAnalyticsClient` — Summarization, Entities & Classification | Reviewed | `begin_abstract_summary()` + `.result()` (paraphrased); `recognize_pii_entities()` (masking) vs. `recognize_linked_entities()` (Wikipedia URLs); `begin_multi_label_classify()` (multiple labels per doc). |
| 2026-11-23 | SDK Walkthrough (#4) | Azure Speech SDK — Real-Time Voice Kiosk STT | Correct | Pair `SpeechConfig` + `SpeechRecognizer` to convert live microphone audio into text (`SpeechSynthesizer` is TTS). |
| 2026-11-23 | MeasureUp | `FileSearchTool` Citations & Retrieved Passage Text (`azure-ai-agents` v1.1.0) | Reviewed → Decoded | Replace `annotation.text` via `annotation.file_citation.file_id`; list run steps with `include=RunAdditionalFieldList.FILE_SEARCH_CONTENTS` and read `results[*].content[*].text`. |
| 2026-11-24 | MeasureUp | OpenTelemetry Tracing & Application Insights (Function Tool Debugging) | Missed → Decoded | Inspect `tool.call.arguments` on the `execute_tool` span for live runtime inputs (`tool_definitions` is static; thread messages hide raw tool calls). |
| 2026-11-24 | MeasureUp | Passwordless Managed Identity Auth — Speech SDK (`FromEndpoint`) & Vision HTTP 401 | Missed → Decoded | Entra ID / Managed Identity requires 3 things: `TokenCredential` (`DefaultAzureCredential`/`ManagedIdentityCredential`), least-privilege RBAC role, and a **Custom Subdomain** (`https://<name>.cognitiveservices.azure.com` — generic `<region>.api.cognitive.microsoft.com` returns `401`). |
| 2026-11-24 | MeasureUp | Azure Content Understanding — Custom Video Analyzer (`returnDetails` vs. `enableSegment`) | Missed → Decoded | Set `returnDetails: true` for granular technical metadata like `cameraShotTimesMs`; `enableSegment` + `contentCategories` splits by topic/chapter; `baseAnalyzerId` can ONLY be one of the 4 base analyzers. |
| 2026-11-24 | MeasureUp | Azure Content Understanding — REST `202` Polling & Typed JSON Path (`prebuilt-invoice`) | Correct → Deepened | Read `result.contents[0].fields.AmountDue.valueObject.Amount.valueNumber` (`contents[0]` list, `fields` sibling of `pages`, typed `valueObject`/`valueNumber` properties, no generic `.value`). |

---

## Decoded MeasureUp Flashcards

### Flashcard 1: Audio + Text Output on Chat Completions Endpoint
* **Scenario:** App sends `input_audio` to an audio-enabled **chat completions** deployment and needs **both spoken audio and text** in the response.
* **Correct Pattern:** Add `"audio"` to the `modalities` array (`["text", "audio"]`) and set `voice` and `format` inside the `audio` object (`{"voice": "...", "format": "wav"}`).
* **Traps to Avoid:**
  * Default `modalities` is `["text"]` only — omitting `"audio"` returns text only.
  * `session.update` is for the **Realtime WebSocket API**, NOT the chat completions endpoint.
  * Top-level `voice` + `response_format` is for standalone TTS, not Chat Completions.

### Flashcard 2: Transcribing a Long Recording (`meeting1.wav`, 20 min) With Azure Speech SDK
* **Scenario:** Script calls `speech_recognizer.recognize_once_async().get()` on a 20-minute `.wav` file and only gets the first sentence.
* **Correct Pattern:** Call **`start_continuous_recognition()`** and collect final text from the **`recognized`** event (past tense = final completed sentence).
* **Traps to Avoid:**
  * `recognize_once_async()` / `recognize_once()` stops after **one single utterance** (~15–30s / first pause).
  * `Speech_SegmentationStrategy = Semantic` only changes how pauses are detected; it does **not** make `recognize_once` process a whole 20-minute file.
  * `recognizing` (present tense `-ing`) fires noisy **partial/in-progress** guesses, NOT final sentences (`recognized`).

### Flashcard 3: SSML `<voice>` Element Overrides `SpeechConfig`
* **Scenario:** App sets `speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"` on `SpeechConfig`, then calls **`speak_ssml_async()`** with SSML documents containing a `<voice>` element—and a different voice speaks!
* **Correct Cause:** The `<voice name="...">` element inside each SSML document specifies a different voice. **SSML always overrides `SpeechConfig`** voice and language settings when using `speak_ssml_async()`.
* **Traps to Avoid:**
  * `mstts:express-as` (`style` / `role`) only changes emotion/delivery (e.g., cheerful, empathetic), NOT which voice is used.
  * `endpoint_id` is only required for **Custom Neural Voices**, not standard prebuilt voices like `AvaMultilingualNeural`.
  * `speech_synthesis_language` is lower priority than `speech_synthesis_voice_name`, and both are ignored when SSML specifies `<voice>`.

### Flashcard 4: Answering Questions About a Private Uploaded Photo (OpenAI Python SDK)
* **Scenario:** User uploads a photo (NOT published to the internet) and asks a question about it; app must return a natural-language answer.
* **2 Correct Actions:**
  1. Call **`chat/completions`** on the **vision-enabled chat model** deployment.
  2. Attach the uploaded file to the user message as an **`image_url`** content part (using a **Base64 data URL** like `data:image/jpeg;base64,...` so it stays private and never needs a public internet URL!).
* **Traps to Avoid:**
  * `images/generations` **creates/draws new images** from text (like DALL-E / GPT-Image)—it does **not** answer questions about an uploaded photo!
  * `Image Analysis 4.0 Caption` only produces a generic 1-sentence description—it cannot answer a custom user question.
  * `Multimodal embeddings` only returns numeric vectors for search/similarity—not a text answer.

### Flashcard 5: `FileSearchTool` Citations & Retrieved Passage Text (`azure-ai-agents` v1.1.0)
* **Scenario:** Foundry agent uses `FileSearchTool` over uploaded policy documents (`files.upload_and_poll`). Replies show placeholder markers instead of filenames, and reviewers also need the exact retrieved passage text.
* **2 Correct Actions:**
  1. **Citations (Replace placeholders):** Replace each `annotation.text` in the message text with the filename resolved from **`annotation.file_citation.file_id`**.
  2. **Retrieved Passage Text:** List the **run steps** with **`include` set to `RunAdditionalFieldList.FILE_SEARCH_CONTENTS`** and read **`results[*].content[*].text`**.
* **Traps to Avoid:**
  * Listing run steps with **default parameters** omits the passage text (`content[*].text`) to save bandwidth.
  * `message.url_citation_annotations` is for **web/Bing grounding URLs**, not uploaded vector-store files.
  * `message.attachments[*].file_id` refers to attached files (e.g., user uploads or Code Interpreter outputs), not inline `FileSearchTool` citations.

### Flashcard 6: Debugging Foundry Agent Function Calls With OpenTelemetry & Application Insights
* **Scenario:** A Foundry project is connected to **Application Insights** with **OpenTelemetry tracing** enabled. An agent with two function tools sometimes calls the wrong tool; you must inspect which function ran and the exact values passed in an affected run.
* **Correct Answer:** Review the **`tool.call.arguments` attribute of the `execute_tool` span**.
* **Plain-English Bank QA Analogy:**
  * **Application Insights** = Azure's audit vault & dashboard (opt-in: must be connected to the Foundry project).
  * **OpenTelemetry** = Standardized audit recorder (opt-in: enabled in SDK code; content recording is controlled separately to protect banking PII).
  * **Trace → Span → Attribute:** Full customer call (`Trace`) → One timed action step (`Span`: `invoke_agent` outer wrapper vs. `execute_tool` actual function call) → Filled-in ticket field (`Attribute`: `tool.call.arguments` = live runtime values!).
* **Traps to Avoid:**
  * `tool_definitions` (on `invoke_agent` span or agent config) is a **static blueprint/menu** — identical across every run, so it never shows what ran during a buggy call.
  * **Thread messages** only store the customer-facing chat transcript and hide internal function call payloads.

### Flashcard 7: The Passwordless Auth 3-Part Formula (`TokenCredential` + `RBAC` + `Custom Subdomain`)
* **Scenarios Covered (Both Speech C# SDK & Vision Python SDK):**
  * **Speech (VM1 + Managed Identity, keys disabled):** Use **`SpeechConfig.FromEndpoint(Uri, TokenCredential)`** — NOT `FromEndpoint(Uri, String)` or `FromSubscription(String, String)` (both pass a banned API key `String`), and NOT `FromAuthorizationToken(String, String)` (a 10-minute manual paper visitor pass that does NOT auto-refresh from VM1's Managed Identity).
  * **Vision (`ImageAnalysisClient` + `DefaultAzureCredential()` returning `HTTP 401`):** `VISION_ENDPOINT` pointed to the generic regional URL (`https://eastus.api.cognitive.microsoft.com`). Fix: **Generate a custom subdomain** (`https://<name>.cognitiveservices.azure.com`) and update `VISION_ENDPOINT`.
* **The 3-Part Enterprise / Banking Formula:**
  1. **Badge (`TokenCredential`):** `DefaultAzureCredential()` / `ManagedIdentityCredential` (auto-refreshes Entra ID tokens; zero hardcoded secrets; gold standard for production vs. API keys in Key Vault/dev).
  2. **Job Title (`RBAC Role`):** Least-privilege role (e.g., `Cognitive Services User`, `Cognitive Services Speech User`).
  3. **Private Street Address (`Custom Subdomain`):** `https://<name>.cognitiveservices.azure.com` — **required** by Microsoft Entra ID (generic `<region>.api.cognitive.microsoft.com` works with API keys ONLY!).
* **HTTP Status Codes to Remember:** **`200 OK`** (success) | **`401 Unauthorized`** (identity/door rejected — bad key, expired token, or Entra ID sent to generic regional URL) | **`403 Forbidden`** (valid identity, missing RBAC role permission).
* **Extra Trap:** Never point standalone **`ImageAnalysisClient`** to a **Foundry Project Endpoint** (`/api/projects/...`) — Project endpoints belong to **`AIProjectClient`**.

### Flashcard 8: Azure Content Understanding — Custom Analyzer 3-Switch Rule (`returnDetails` vs. `enableSegment`)
* **Scenario:** Custom analyzer extends `prebuilt-video` with `enableSegment: false` and `returnDetails` unset. A video-editing app needs the timestamp of every camera shot change (`cameraShotTimesMs`).
* **Correct Answer:** Set **`returnDetails` to `true`**.
* **3-Switch Mental Model (Properties in the Analyzer JSON Definition — NOT methods!):**
  * **`baseAnalyzerId`** — Custom analyzers can **ONLY** extend the **4 Base Analyzers** (`prebuilt-document`, `prebuilt-image`, `prebuilt-audio`, `prebuilt-video`) — **NEVER** RAG analyzers like `prebuilt-videoSearch` or `prebuilt-documentSearch`!
  * **`enableSegment: true` + `contentCategories`** — Splits content by **business meaning / topic chapters / mixed document types** using the generative model (a matched pair; `contentCategories` does nothing when `enableSegment` is `false`).
  * **`returnDetails: true`** — Unlocks **granular technical metadata** omitted by default, such as `cameraShotTimesMs` (video camera cut timestamps in ms) or detailed document layout coordinates.

### Flashcard 9: Content Understanding REST API `202` Polling & Typed JSON Response Paths
* **Scenario:** App calls `prebuilt-invoice` via REST API (`POST` → `HTTP 202 Accepted` + `Operation-Location` polling until `Succeeded` — the exact mechanism `begin_analyze()` + `poller.result()` wraps in Python!). Need the numeric `AmountDue` from JSON.
* **Correct Path:** **`result.contents[0].fields.AmountDue.valueObject.Amount.valueNumber`**
* **Behind-the-Scenes Rules:**
  * **`contents[0]` is required:** Because an analysis job can return multiple documents/segments, `fields` lives inside each item of the `contents` array (0-indexed), NOT directly under `result`.
  * **`fields` is a sibling of `pages`:** Document-level extracted fields belong to `contents[0].fields`, NOT `pages[0].fields` (`pages` holds physical layout: width, height, angle, words).
  * **Typed value properties (no generic `.value`):** Azure stamps the data type onto the key — **`valueObject`** (sub-field bundle), **`valueNumber`** (number), **`valueString`** (text), **`valueDate`** (date).
  * **JSON Naming Tip:** `camelCase` (`result`, `contents`, `fields`, `valueObject`, `valueNumber`) = Azure's standard structural envelope keys; `PascalCase` (`AmountDue`, `Amount`, `CurrencyCode`) = domain/business field names defined by the analyzer's schema (`prebuilt-invoice`).
  * **Universal SDK ↔ JSON Rule:** Python (`snake_case`), C# (`PascalCase`), and REST APIs all translate to/from **JSON messages over HTTPS** under the hood — no `.json` file on disk is required.
