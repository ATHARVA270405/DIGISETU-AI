import re
from urllib.parse import urljoin

import requests


class ContactEnricher:

    def enrich(self, lead: dict[str, object]) -> dict[str, object]:

        email = lead.get("email", "")
        website = lead.get("website", "")

        if not email and website:
            email = self._find_email(website)

        return {
            "name": lead.get("name", ""),
            "business_type": lead.get("business_type", ""),
            "email": email,
            "phone": lead.get("phone", ""),
            "website": website,
            "location": lead.get("location", ""),
        }

    def _find_email(self, website: str) -> str:

        pages = [
            website,
            urljoin(website, "/contact"),
            urljoin(website, "/contact-us"),
            urljoin(website, "/about"),
            urljoin(website, "/about-us"),
        ]

        for page in pages:

            try:
                response = requests.get(
                    page,
                    timeout=5,
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    },
                )

                if response.status_code >= 400:
                    continue

                emails = re.findall(
                    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                    response.text,
                )

                if emails:
                    return emails[0]

            except requests.RequestException:
                continue

        return ""