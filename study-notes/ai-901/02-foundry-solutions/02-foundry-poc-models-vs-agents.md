---
id: ai901-d2-02
title: "Azure AI Foundry POC Summary: Models vs. Agents & Endpoints"
exam: AI-901
domain: "Domain 2: Implement AI Solutions Using Microsoft Foundry"
topics:
  - Azure CLI Authentication
  - Project Endpoint vs Azure OpenAI Endpoint
  - Stateless Models vs Stateful Agents
  - Multi-Turn Conversations
keywords:
  - az login
  - FOUNDRY_PROJECT_ENDPOINT
  - Azure OpenAI Endpoint
  - stateful agent
  - stateless model
  - conversations.create
  - responses.create
  - get_openai_client
  - pyaudio
source: gemini-web-import
last_updated: 2026-11-20
---

# Azure AI Foundry POC Summary

## Overview
This document summarizes the setup, configuration, and architectural takeaways from our proof-of-concept (POC) session connecting Visual Studio Code to Microsoft Azure AI Foundry using Python.

---

## 1. Environment & Authentication Setup
* **Azure CLI Authentication (`az login`):** Authenticated the local terminal with Azure credentials. When prompted for subscription and tenant selection, pressing **Enter** accepts the default active subscription, which is sufficient for a quick POC.
* **Virtual Environments (`.venv`):** Created an isolated Python virtual environment in VS Code.
  * *Best Practice:* Always use a dedicated virtual environment per POC or sandbox to isolate dependencies and prevent version conflicts with global Python installations.
* **Python Version Compatibility:** Decided to proceed with the current local Python version rather than downgrading to Python 3.12. If real-time audio dependencies (like `pyaudio`) present compatibility hurdles on newer Python versions, text-based model/agent interactions serve as a conflict-free baseline test.

---

## 2. Project Configuration & Endpoints
* **File Naming:** Created `poc-app.py` (following Python's lowercase naming conventions; `app.py` or `snake_case.py` are standard).
* **Endpoint Selection:** Identified the difference between the two endpoints available in the Microsoft Foundry portal:
  * **Project Endpoint (`FOUNDRY_PROJECT_ENDPOINT`):** Used by the Foundry SDK to manage the project, agents, and conversation threads. *(Selected for this POC)*
  * **Azure OpenAI Endpoint:** Used for direct, standalone calls to underlying Azure OpenAI LLM deployments.
* **Script Execution:** Replaced the endpoint placeholder in the script and executed it via the integrated terminal using:
  ```bash
  python poc-app.py
  ```

---

## 3. Architectural Takeaways: Models vs. Agents
* **Chatting with a Model (Stateless):** The initial quickstart script sends a hardcoded input string directly to a model (`gpt-5-mini`), returning a single, stateless response.
* **Working with an Agent (Stateful & Contextual):** Connecting to a pre-configured Foundry Agent (such as the *Customer Support / Return-Policy Assistant*) allows you to retain baked-in instructions, personas, and goals.
* **Multi-Turn Conversations:** To maintain chat history across multiple turns without hardcoding inputs:
  1. Initialize the client: `openai = project.get_openai_client(agent_name=FOUNDRY_AGENT_NAME)`
  2. Create a conversation thread: `conversation = openai.conversations.create()`
  3. Pass `conversation.id` into subsequent `openai.responses.create()` calls alongside dynamic user inputs (e.g., via Python's `input()` function).

---

## Next Steps
- [ ] Complete virtual environment initialization in VS Code.
- [ ] Test the agent script (using text-based I/O if bypassing `pyaudio` voice streaming).
- [ ] Implement a `while` loop with `input()` and `conversations.create()` for continuous multi-turn testing.
