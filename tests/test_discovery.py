from digisetu.discovery.service import BusinessDiscoveryService


service = BusinessDiscoveryService()

results = service.discover(
    business_type="Dental Clinic",
    location="Nagpur",
)

print(results)