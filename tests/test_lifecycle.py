from digisetu.management.lifecycle import LeadLifecycleManager


manager = LeadLifecycleManager()

status = "NEW"

events = [
    "QUALIFIED",
    "CONTACTED",
    "REPLIED",
    "INTERESTED",
    "CONVERTED",
]

for event in events:

    status = manager.update_status(
        current_status=status,
        event=event,
    )

    print(f"Event: {event}")
    print(f"Status: {status}")
    print()