import requests
from urllib.parse import urlparse


class WebsiteAudit:

    def audit(self, website: str) -> dict[str, object]:
        if not website:
            return {
                "website_exists": False,
                "https": False,
                "accessible": False,
                "booking": False,
                "payment": False,
                "mobile_friendly": False,
            }

        parsed_url = urlparse(website)

        try:
            response = requests.get(
                website,
                timeout=5,
                allow_redirects=True,
            )

            accessible = response.status_code < 400
            page_content = response.text.lower()

        except requests.RequestException:
            accessible = False
            page_content = ""

        booking_keywords = [
            "book now",
            "booking",
            "appointment",
            "schedule appointment",
            "reserve",
        ]

        payment_keywords = [
            "payment",
            "pay now",
            "checkout",
            "upi",
            "razorpay",
            "stripe",
        ]

        booking = any(
            keyword in page_content
            for keyword in booking_keywords
        )

        payment = any(
            keyword in page_content
            for keyword in payment_keywords
        )

        mobile_friendly = (
            'name="viewport"' in page_content
            or "name='viewport'" in page_content
        )

        return {
            "website_exists": True,
            "https": parsed_url.scheme == "https",
            "accessible": accessible,
            "booking": booking,
            "payment": payment,
            "mobile_friendly": mobile_friendly,
        }