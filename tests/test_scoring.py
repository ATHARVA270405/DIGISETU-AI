from digisetu.audit.scoring import DigitalNeedScorer


scorer = DigitalNeedScorer()

audit_result = {
    "website_exists": True,
    "https": True,
    "accessible": True,
    "booking": False,
    "payment": False,
    "mobile_friendly": True,
}

score = scorer.calculate(audit_result)

print("Digital Need Score:", score)