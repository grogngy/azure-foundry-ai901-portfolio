# POC1 Starter Agent

A minimal Python client that connects to an existing **Microsoft Foundry** agent using **Microsoft Entra ID** (`DefaultAzureCredential`) and sends a conversational prompt through the Foundry Responses API.

## AI-901 Concepts Demonstrated
- **Domain 2:** Authenticating to Microsoft Foundry with `DefaultAzureCredential` (no hardcoded API keys).
- **Domain 2:** Initializing `AIProjectClient` with a Foundry project endpoint and invoking an existing agent.

## How to Run
1. Make sure you have copied `.env.example` to `.env` in the repository root and filled in `AZURE_FOUNDRY_PROJECT_ENDPOINT` and `AZURE_FOUNDRY_POC_AGENT_NAME`.
2. Sign in to Azure:
   ```powershell
   az login
   ```
3. Run the script:
   ```powershell
   python agents/poc1-starter/app.py
   ```
