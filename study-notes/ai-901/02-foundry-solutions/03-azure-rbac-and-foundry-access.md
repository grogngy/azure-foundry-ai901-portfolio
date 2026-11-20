---
id: ai901-d2-03
title: "Azure RBAC & Foundry Resource Permissions Summary"
exam: AI-901
domain: "Domain 2: Implement AI Solutions Using Microsoft Foundry"
topics:
  - Azure RBAC
  - Least Privilege Access
  - Foundry IQ and Workspace Permissions
keywords:
  - Azure RBAC
  - role assignment
  - Foundry IQ
  - least privilege
  - subscription
  - resource group
  - workspace
  - service principal
source: gemini-web-import
last_updated: 2026-11-20
---

# Azure RBAC & Foundry Resource Permissions Summary

## Overview
This document summarizes our discussion regarding how to manage access and assign permissions for **Foundry** services and related AI resources using **Azure Role-Based Access Control (RBAC)**.

---

## Key Concepts

* **Azure RBAC Authorization:** Access to Foundry features and AI resources is governed by standard Azure RBAC principles. Roles are assigned at specific scopes (such as subscriptions, resource groups, or individual workspaces) to control who can manage or interact with those services.
* **Foundry IQ & Related Features:** Just like configuring access for **Foundry IQ**, the same role-assignment workflow applies across other core Foundry and Azure AI capabilities.

---

## Examples of Resources Requiring Similar Role Assignments

When working within the Foundry portal and your development workspace, you will typically need to assign appropriate Azure roles for the following resources:

1. **AI Solution Templates:** Deploying, configuring, and managing pre-built AI solution templates available in the Foundry portal.
2. **Chat Completion Models:** Accessing, testing, and integrating generative AI models (such as **Azure OpenAI** deployments).
3. **Development Environments (Dev Packs):** Setting up, provisioning, and collaborating within development environments and dev packs tied to your workspace.

---

## Next Steps
* Identify the specific target resource (e.g., AI Solution Templates, Chat Completion Models, or Dev Packs).
* Determine the appropriate scope (Workspace or Resource Group) in the Azure Portal.
* Assign the corresponding least-privilege Azure RBAC role to users or service principals.
