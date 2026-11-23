---
id: ai901-quiz-log
title: "AI-901 MeasureUp Practice Quizzes & Decoded Flashcards"
exam: AI-901
domain: "Domain 2: Implement AI Solutions Using Microsoft Foundry"
topics:
  - MeasureUp Error Log
  - Audio Chat Completions
  - Azure Speech SDK Continuous Recognition
keywords:
  - modalities
  - audio object
  - session.update
  - recognize_once_async
  - start_continuous_recognition
  - recognized vs recognizing
  - SpeechConfig
source: measureup-study-log
last_updated: 2026-11-23
---

# AI-901 Practice Quizzes & Review Log

Track practice questions, decoded jargon, and exam traps here so every missed or tricky MeasureUp question turns into permanent RAG study memory.

## Session Log
| Date | Source | Topic | Outcome | Key Takeaway |
| :--- | :--- | :--- | :--- | :--- |
| 2026-11-23 | MeasureUp | Audio-enabled Chat Completions (`modalities` + `audio` object) | Correct | Add `"audio"` to `modalities` array AND set `voice` + `format` in `audio` object. |
| 2026-11-23 | MeasureUp | Azure Speech SDK — Long Audio Transcription (`meeting1.wav`) | Missed → Decoded | Use `start_continuous_recognition()` + `recognized` event (not `recognize_once_async()`). |
| 2026-11-23 | MeasureUp | Azure Speech SDK — SSML `<voice>` Overrides `SpeechConfig` | Missed → Decoded | `speak_ssml_async()` uses the `<voice name="...">` inside the SSML document and ignores `SpeechConfig` voice/language settings. |

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
