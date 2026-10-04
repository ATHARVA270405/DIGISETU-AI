from digisetu.audit.website import WebsiteAudit


audit = WebsiteAudit()

result = audit.audit("https://example.com")

print(result)