# Text-to-Image POC Agent

An interactive Python client connected to a **Microsoft Foundry** multimodal prompt agent for **text-to-image prompt engineering and visual content generation workflows**.

## AI-901 Concepts Demonstrated
- **Domain 1 & 2:** Generative vision / image generation workloads in Microsoft Foundry.
- **Domain 2:** Multi-turn Foundry SDK client (`AIProjectClient`, `DefaultAzureCredential`, and `.env` configuration hygiene).

## How to Run
1. Copy `.env.example` to `.env` in the repository root and set `AZURE_FOUNDRY_PROJECT_ENDPOINT` and `AZURE_FOUNDRY_TEXT_TO_IMAGE_AGENT_NAME`.
2. Sign in to Azure:
   ```powershell
   az login
   ```
3. Run the interactive client:
   ```powershell
   python agents/text-to-image-agent/app.py
   ```
