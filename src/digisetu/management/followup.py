class FollowUpManager:

    def decide(self, intent: str) -> str:

        intent = intent.strip().upper()

        if intent == "INTERESTED":
            return "FOLLOW_UP"

        if intent == "QUESTION":
            return "RESPOND_AND_FOLLOW_UP"

        if intent == "NOT_INTERESTED":
            return "STOP"

        return "REVIEW"