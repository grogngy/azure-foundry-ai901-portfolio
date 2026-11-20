---
id: ai901-d2-01
title: "Azure AI Foundry & VS Code Setup Summary"
exam: AI-901
domain: "Domain 2: Implement AI Solutions Using Microsoft Foundry"
topics:
  - Microsoft Foundry SDK Quickstart
  - Local Workspace Setup
  - Microsoft Learn Resources
keywords:
  - Microsoft Foundry SDK
  - AI-901
  - VS Code
  - quickstart
  - generative AI apps
source: gemini-web-import
last_updated: 2026-11-20
---

# Azure AI Foundry & VS Code Setup Summary

## Project Goal
* **Objective:** Build simple, hands-on proof-of-concept (PoC) web applications to reinforce theoretical knowledge for the **Azure AI Fundamentals (Exam AI-901)** certification.
* **Approach:** Keep the setup minimal ("ABC for dummies" / baby steps) using **Visual Studio Code**, **GitHub Copilot**, and the **Microsoft Foundry SDK** (Python), saving complex infrastructure and advanced frontend designs for later iterations.

---

## Recommended Learning Resources
To get hands-on quickly without getting bogged down in complex configurations, use these official, free Microsoft Learn resources:
1. **Quickstart:** *Get started with Microsoft Foundry SDK* (Best starting point for environment setup, package installation, and running a first model call).
2. **Learning Path:** *Develop generative AI apps on Microsoft Foundry* (Great follow-up for structured learning).

---

## Workspace & Environment Best Practices
Before jumping into the Microsoft Learn Python steps, set up your local environment cleanly to avoid command-line and SDK path-length errors:

1. **Create a Short Root Directory:**
   * **Windows:** `C:\Projects`
   * **macOS:** `~/Projects`
2. **Create Your Project Folder:**
   * Place your specific project folder inside the root directory (e.g., `C:\Projects\foundry-poc`).
   * **Rule:** Avoid spaces in folder names (use hyphens `-` or underscores `_`).
3. **Open in VS Code:**
   * Launch Visual Studio Code and open your newly created project folder (`File > Open Folder`).

---

## Next Steps (Action Plan)
1. **Initialize Folder:** Open your clean, short-path project directory in VS Code.
2. **Follow the Quickstart:** Use the *Get started with Microsoft Foundry SDK* guide on Microsoft Learn.
3. **Install Dependencies:** Set up your Python environment and install the required Azure AI SDK packages via the VS Code terminal.
4. **Authenticate & Run:** Configure your API keys/credentials and execute your first model call, leveraging VS Code and Copilot to inspect and understand the code behind the scenes.
