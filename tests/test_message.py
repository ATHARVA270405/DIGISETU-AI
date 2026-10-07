from digisetu.enrichment.message import MessageGenerator


generator = MessageGenerator()

lead = {
    "name": "ABC Dental Clinic",
    "business_type": "Dental Clinic",
    "location": "Nagpur",
    "website": "https://example.com",
}

qualification = {
    "digital_need_score": 35,
    "qualified": True,
    "digital_gaps": [
        "booking",
        "payment",
    ],
    "reason": "Insufficient booking and payment features on the website.",
}

message = generator.generate(
    lead=lead,
    qualification=qualification,
)

print("\nGenerated Message:\n")
print(message)