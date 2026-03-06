import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"

def extract_with_llm(transcript, account_id):

    prompt = f"""
Extract structured account configuration from this transcript.

Return JSON with fields:

company_name
business_hours
services_supported
emergency_definition
integration_constraints
questions_or_unknowns
notes

Do not guess missing information.

Transcript:
{transcript}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    try:
        data = json.loads(result)
    except:
        data = {"notes": result}

    data["account_id"] = account_id

    return data