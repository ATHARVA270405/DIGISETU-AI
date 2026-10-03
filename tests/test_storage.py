from digisetu.discovery.storage import LeadStorage


storage = LeadStorage()

lead = {
    "name": "ABC Dental Clinic",
    "business_type": "Dental Clinic",
    "address": "Nagpur",
    "phone": "",
    "website": "",
    "location": "Nagpur",
    "source": "demo",
}

storage.save(lead)

print("Lead saved successfully.")