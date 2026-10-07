from digisetu.enrichment.contact import ContactEnricher


enricher = ContactEnricher()

lead = {
    "name": "ABC Dental Clinic",
    "business_type": "Dental Clinic",
    "phone": "9876543210",
    "website": "https://example.com",
    "location": "Nagpur",
}

result = enricher.enrich(lead)

print("Enriched Lead:")
print(result)