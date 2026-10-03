class BusinessDataExtractor:

    def extract(
        self,
        raw_business: dict[str, str],
    ) -> dict[str, str]:
        return {
            "name": raw_business.get("name", ""),
            "business_type": raw_business.get("business_type", ""),
            "address": raw_business.get("address", ""),
            "phone": raw_business.get("phone", ""),
            "website": raw_business.get("website", ""),
            "location": raw_business.get("location", ""),
            "source": raw_business.get("source", ""),
        }