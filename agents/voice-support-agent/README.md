# Realtime Voice Customer Support Agent

A hands-free, bidirectional voice client connecting to a **Microsoft Foundry** realtime voice agent with microphone capture, live speech transcription, and barge-in interruption support.

## AI-901 Concepts Demonstrated
- **Domain 1 & 2:** Speech and realtime multimodal AI workloads in Microsoft Foundry.
- **Domain 2:** Async Foundry SDK (`azure.ai.projects.aio`), Entra ID auth, and externalized environment configuration.

## How to Run
1. Copy `.env.example` to `.env` in the repository root and set `AZURE_FOUNDRY_PROJECT_ENDPOINT` and `AZURE_FOUNDRY_VOICE_AGENT_NAME`.
2. Sign in to Azure:
   ```powershell
   az login
   ```
3. Plug in a headset (to prevent echo) and run:
   ```powershell
   python agents/voice-support-agent/app.py
   ```
