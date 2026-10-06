import requests


class QualificationAgent:

    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "llama3.2"

    def qualify(
        self,
        business: dict[str, object],
        audit: dict[str, object],
        score: int,
    ) -> dict[str, object]:

        prompt = f"""
You are the DigiSetu Qualification Agent.

Analyze the business using ONLY the information provided below.

Business:
{business}

Website Audit:
{audit}

Digital Need Score:
{score}

Rules:
- Qualify the business if the Digital Need Score is 40 or higher.
- Do NOT invent digital gaps.
- Only mention gaps that can be directly identified from the Website Audit.
- Do NOT add e-commerce, SEO, social media, or other features unless they are explicitly present in the audit.
- Keep the reason short.

Return EXACTLY in this format:

QUALIFIED: YES or NO
DIGITAL_GAPS: gap1, gap2, gap3
REASON: short explanation
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

        result = response.json()["response"].strip()

        return self._parse_result(
            business=business,
            score=score,
            result=result,
        )

    def _parse_result(
        self,
        business: dict[str, object],
        score: int,
        result: str,
    ) -> dict[str, object]:

        qualified = False
        digital_gaps = []
        reason = ""

        for line in result.splitlines():

            line = line.strip()

            if line.startswith("QUALIFIED:"):
                qualified = "YES" in line.upper()

            elif line.startswith("DIGITAL_GAPS:"):
                gaps = line.split(":", 1)[1].strip()

                if gaps:
                    digital_gaps = [
                        gap.strip()
                        for gap in gaps.split(",")
                    ]

            elif line.startswith("REASON:"):
                reason = line.split(":", 1)[1].strip()

        return {
            "business_name": business.get("name", ""),
            "digital_need_score": score,
            "qualified": qualified,
            "digital_gaps": digital_gaps,
            "reason": reason,
        }