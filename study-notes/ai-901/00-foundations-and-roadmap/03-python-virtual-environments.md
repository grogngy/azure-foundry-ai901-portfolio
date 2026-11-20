---
id: ai901-fnd-03
title: "Learning Notes: Azure AI Fundamentals & Python Virtual Environments"
exam: AI-901
domain: "Cross-Domain (Developer Foundations)"
topics:
  - Python Virtual Environments
  - Dependency Isolation
  - Workspace Hygiene
keywords:
  - venv
  - Python
  - virtual environment
  - dependencies
  - VS Code terminal
source: gemini-web-import
last_updated: 2026-11-20
---

# Learning Notes: Azure AI Fundamentals & Python Virtual Environments

## Current Status & Context
* **Certification Goal:** Currently studying and preparing to take the **Microsoft Azure AI Fundamentals** exam.
* **Development Background:** Basic development knowledge; currently building **Proof of Concepts (PoCs)** to gain hands-on experience.
* **Tooling Strategy:** Leveraging AI assistants (Gemini and GitHub Copilot in Visual Studio Code) to learn step-by-step and navigate technical concepts.

---

## Key Technical Takeaways: Python Virtual Environments

### 1. What is a Virtual Environment?
* A Python virtual environment (`venv`) is an isolated workspace that keeps a specific Python installation and its installed libraries separate from the global system and other projects.
* **Why it matters:** It prevents dependency conflicts when different projects or PoCs require different versions of the same library.

### 2. Managing Multiple Virtual Environments
* Having multiple virtual environments is normal when working on different projects or PoCs.
* **Should you delete one?**
  * **Keep it** if it is tied to a specific, active PoC with unique dependencies.
  * **Delete it** if it was created by mistake, is an exact duplicate, or belongs to a completed experiment you no longer need.

### 3. Using Copilot vs. Terminal in VS Code
* **Best Practice:** Manage, activate, and delete virtual environments directly through the **VS Code Terminal** (e.g., deleting the environment folder once deactivated) rather than relying on GitHub Copilot to execute file/folder deletions.
* Use Copilot primarily for writing code, explaining error messages, and learning syntax within your PoCs.
