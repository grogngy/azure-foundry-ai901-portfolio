"""
Interactive multi-turn client for the Finance Expenses Assistant agent
hosted in Microsoft Foundry.

Prerequisites:
    pip install "azure-ai-projects>=2.1.0" "azure-identity>=1.17.0,<2.0.0"
    az login
"""

import os
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential


def load_local_env() -> None:
    """Load key=value pairs from the repository root .env file if present."""
    env_path = Path(__file__).resolve().parents[2] / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def main() -> None:
    load_local_env()

    endpoint = os.environ.get("AZURE_FOUNDRY_PROJECT_ENDPOINT")
    agent_name = os.environ.get("AZURE_FOUNDRY_EXPENSES_AGENT_NAME")

    if not endpoint or not agent_name:
        raise RuntimeError(
            "Missing AZURE_FOUNDRY_PROJECT_ENDPOINT or AZURE_FOUNDRY_EXPENSES_AGENT_NAME in .env."
        )

    with (
        DefaultAzureCredential() as credential,
        AIProjectClient(
            endpoint=endpoint,
            credential=credential,
            allow_preview=True,
        ) as project_client,
    ):
        openai_client = project_client.get_openai_client(agent_name=agent_name)
        conversation = openai_client.conversations.create()

        print(f"Connected to Expenses Agent: {agent_name}")
        print("Ask about expense policies, claims, or validations (type 'exit' to quit).\n")

        while True:
            user_message = input("You: ").strip()
            if not user_message:
                continue
            if user_message.lower() in {"exit", "quit"}:
                print("Ending session.")
                break

            response = openai_client.responses.create(
                conversation=conversation.id,
                input=[{"role": "user", "content": user_message}],
            )
            print(f"\nExpenses Agent: {response.output_text}\n")


if __name__ == "__main__":
    main()
