# Finance Expenses Assistant Agent

A stateful, multi-turn Python client connected to a **Microsoft Foundry** prompt agent designed for **expense policy guidance, claim checks, and financial workflow automation**—bridging banking/finance domain expertise with Azure AI engineering.

## AI-901 Concepts Demonstrated
- **Domain 1 & 2:** Stateful single-agent solution with persistent conversation context (`conversations.create()` + `responses.create()`).
- **Domain 2:** Passwordless Microsoft Entra ID authentication (`DefaultAzureCredential`) and shared Foundry Project Endpoint configuration via `.env`.

## How to Run
1. Copy `.env.example` to `.env` in the repository root and set `AZURE_FOUNDRY_PROJECT_ENDPOINT` and `AZURE_FOUNDRY_EXPENSES_AGENT_NAME`.
2. Sign in to Azure:
   ```powershell
   az login
   ```
3. Run the interactive client:
   ```powershell
   python agents/expenses-agent/app.py
   ```
