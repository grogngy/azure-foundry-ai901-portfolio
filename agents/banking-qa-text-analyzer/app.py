"""
AI-901 Hands-On SDK Lab: Banking QA Ticket Triage & PII Redactor (Privacy-First Pipeline)
Uses the official Azure AI Language / Text Analytics Python SDK
(azure-ai-textanalytics) in a chained, fail-closed Responsible AI pipeline:
  Step 1: Redact Personally Identifiable Information (PII) FIRST (`recognize_pii_entities`)
  Step 2: Pass ONLY the redacted text to Sentiment Analysis & Key Phrase Extraction
  Step 3: Run an automated QA leak check verifying zero PII entities appear downstream

Prerequisites:
    pip install azure-ai-textanalytics azure-identity
    az login   (or set AZURE_LANGUAGE_KEY in .env)
"""

import os
from pathlib import Path

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
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


def create_text_analytics_client() -> TextAnalyticsClient:
    """
    Initialize TextAnalyticsClient using either:
      - AzureKeyCredential (if AZURE_LANGUAGE_KEY is provided in .env), OR
      - DefaultAzureCredential (passwordless Microsoft Entra ID via `az login`).
    """
    endpoint = os.environ.get("AZURE_LANGUAGE_ENDPOINT")
    api_key = os.environ.get("AZURE_LANGUAGE_KEY")

    if not endpoint:
        raise RuntimeError(
            "Missing AZURE_LANGUAGE_ENDPOINT in .env. "
            "Set it to your Azure AI Services / Foundry resource endpoint."
        )

    credential = AzureKeyCredential(api_key) if api_key else DefaultAzureCredential()
    return TextAnalyticsClient(endpoint=endpoint, credential=credential)


def check_pii_leaks(pii_entities: list, redacted_text: str, key_phrases: list[str]) -> list[str]:
    """Return any detected PII values that still appear in redacted text or key phrases."""
    downstream_blob = (redacted_text + " " + " ".join(key_phrases)).lower()
    leaks = []
    for entity in pii_entities:
        token = entity.text.strip()
        if token and token.lower() in downstream_blob:
            leaks.append(f"{entity.category}:{token}")
    return leaks


def main() -> None:
    load_local_env()
    client = create_text_analytics_client()

    # Sample synthetic banking QA tickets (NO real customer data!)
    sample_tickets = [
        (
            "Hi, my name is Maria Lopez (maria.lopez@example.com, 555-019-2834). "
            "I was charged a duplicate wire transfer fee on account 4421980012 and "
            "nobody has resolved my dispute after three calls. Very frustrated!"
        ),
        (
            "Just wanted to thank the branch team for quickly resetting my online "
            "banking PIN and explaining the new Zelle daily transfer limits clearly."
        ),
    ]

    print("=== Banking QA Ticket Triage & PII Redactor (Privacy-First Pipeline) ===\n")

    # STEP 1: Redact PII FIRST (fail-closed: never forward raw text if PII check errors)
    pii_results = client.recognize_pii_entities(sample_tickets)
    safe_tickets = [
        pii.redacted_text if not pii.is_error else ""
        for pii in pii_results
    ]

    # STEP 2: Run downstream NLP ONLY on redacted text so PII never leaks into tags/logs
    sentiment_results = client.analyze_sentiment(safe_tickets)
    phrase_results = client.extract_key_phrases(safe_tickets)

    for idx, (pii, sentiment, phrases) in enumerate(
        zip(pii_results, sentiment_results, phrase_results), start=1
    ):
        print(f"--- Ticket #{idx} ---")
        if not pii.is_error:
            print(f"Redacted Text     : {pii.redacted_text}")
            detected = [f"{e.category} ({e.confidence_score:.0%})" for e in pii.entities]
            print(f"PII Detected      : {', '.join(detected) if detected else 'None'}")
        else:
            print(f"PII Error         : {pii.error.message} (Fail-closed: downstream skipped)")
            print()
            continue

        if not sentiment.is_error:
            scores = sentiment.confidence_scores
            print(
                f"Sentiment         : {sentiment.sentiment.upper()} "
                f"(pos={scores.positive:.2f}, neu={scores.neutral:.2f}, neg={scores.negative:.2f})"
            )
            priority = "HIGH (Escalate to QA Lead)" if sentiment.sentiment == "negative" else "NORMAL"
            print(f"QA Priority       : {priority}")
        else:
            print(f"Sentiment Error   : {sentiment.error.message}")

        extracted_phrases = phrases.key_phrases if not phrases.is_error else []
        if not phrases.is_error:
            print(f"Key Phrases (Safe): {', '.join(extracted_phrases)}")
        else:
            print(f"Key Phrases Error : {phrases.error.message}")

        # STEP 3: Automated QA Leak Verification
        leaks = check_pii_leaks(pii.entities, pii.redacted_text, extracted_phrases)
        if not leaks:
            print("QA PII Leak Check : PASS (0 leaked entities in downstream outputs)")
        else:
            print(f"QA PII Leak Check : FAIL ({', '.join(leaks)})")
        print()


if __name__ == "__main__":
    main()
