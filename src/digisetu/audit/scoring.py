class DigitalNeedScorer:

    def calculate(self, audit: dict[str, object]) -> int:
        score = 0

        if not audit.get("website_exists", False):
            score += 30

        if not audit.get("https", False):
            score += 15

        if not audit.get("mobile_friendly", False):
            score += 20

        if not audit.get("booking", False):
            score += 15

        if not audit.get("payment", False):
            score += 20

        return score