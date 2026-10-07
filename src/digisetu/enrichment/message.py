import requests


class MessageGenerator:

    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "llama3.2"

    def generate(
        self,
        lead: dict[str, object],
        qualification: dict[str, object],
    ) -> str:

        if not qualification.get("qualified", False):
            return ""

        prompt = f"""
You are the DigiSetu outreach message generator.

Create a short, professional and personalized business outreach message.

Business:
{lead}

Qualification:
{qualification}

Rules:
- Mention the business name.
- Mention only the digital gaps provided in the qualification.
- Explain briefly how solving those gaps could help the business.
- Do not invent business facts.
- Do not make unrealistic promises.
- Mention only facts and digital gaps explicitly provided in the input.
- Do not claim that DigiSetu provides, implements, or sells any service.
- Do not mention growth, retention, referrals, revenue, efficiency, or customer satisfaction unless explicitly provided in the input.
- Do not invent benefits or business outcomes.
- Do not say "our solutions", "our team", or "we can implement".
- Keep the message focused on identifying the digital gaps and asking whether the business would like to discuss them.
- Do not claim that DigiSetu has an expert team or provides services unless explicitly stated in the input.
- Do not claim that DigiSetu can implement any solution unless explicitly stated in the input.
- Do not sound like spam.
- Keep the message under 150 words.
- Include a simple call to action.
- Return only the message.
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

        return response.json()["response"].strip()