from digisetu.discovery.extractor import BusinessDataExtractor


extractor = BusinessDataExtractor()

raw_business = {
    "name": "ABC Dental Clinic",
    "business_type": "Dental Clinic",
    "location": "Nagpur",
}

result = extractor.extract(raw_business)

print(result)