from digisetu.qualification import QualificationAgent


agent = QualificationAgent()

business = {
    "name": "ABC Dental Clinic",
    "business_type": "Dental Clinic",
    "location": "Nagpur",
}

audit = {
    "website_exists": True,
    "https": True,
    "accessible": True,
    "booking": False,
    "payment": False,
    "mobile_friendly": True,
}

score = 35

result = agent.qualify(
    business=business,
    audit=audit,
    score=score,
)

print("\nQualification Result:")
print(result)