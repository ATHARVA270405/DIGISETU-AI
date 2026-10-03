class BusinessDiscoveryService:

    def discover(
        self,
        business_type: str,
        location: str,
    ) -> list[dict[str, str]]:
        return [
            {
                "name": "Demo Business",
                "business_type": business_type,
                "location": location,
            }
        ]