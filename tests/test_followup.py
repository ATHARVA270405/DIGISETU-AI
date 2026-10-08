from digisetu.management.followup import FollowUpManager


manager = FollowUpManager()

intents = [
    "INTERESTED",
    "QUESTION",
    "NOT_INTERESTED",
    "OTHER",
]

for intent in intents:

    action = manager.decide(intent)

    print(f"Intent: {intent}")
    print(f"Action: {action}")
    print()