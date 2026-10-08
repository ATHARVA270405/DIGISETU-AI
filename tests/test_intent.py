from digisetu.management.intent import IntentDetector


detector = IntentDetector()

replies = [
    "Yes, we are interested. Please send us more information.",
    "Thank you, but we are not interested.",
    "Can you tell me how much this service costs?",
    "Thanks for contacting us. Have a great day.",
]

for reply in replies:

    intent = detector.detect(reply)

    print("\nReply:")
    print(reply)

    print("Intent:")
    print(intent)