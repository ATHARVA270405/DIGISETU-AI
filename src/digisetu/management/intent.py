import requests


class IntentDetector:

    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "llama3.2"

    def detect(self, reply: str) -> str:

        prompt = f"""
You are the DigiSetu Reply Intent Detection Agent.

Analyze the business email reply below.

Business Reply:
{reply}

Classify the reply into EXACTLY ONE of these categories:

INTERESTED
NOT_INTERESTED
QUESTION
OTHER

Rules:
- INTERESTED = business shows interest in discussing or using the service.
- NOT_INTERESTED = business clearly rejects or declines.
- QUESTION = business mainly asks for information or clarification.
- OTHER = unclear, unrelated, or cannot be classified.
- Do NOT assume rejection from a polite or neutral reply.
- If the reply does not clearly show interest or rejection, classify it as OTHER.

Return ONLY the category name.
"""

        response = requests.post(
            self.ollama_url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        result = response.json()["response"].strip().upper()

        allowed_intents = {
            "INTERESTED",
            "NOT_INTERESTED",
            "QUESTION",
            "OTHER",
        }

        if result not in allowed_intents:
            return "OTHER"

        return result