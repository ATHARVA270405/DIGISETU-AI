class EmailSender:

    def send(
        self,
        recipient: str,
        subject: str,
        message: str,
    ) -> bool:

        print("\n--- EMAIL ---")
        print(f"To: {recipient}")
        print(f"Subject: {subject}")
        print(f"Message:\n{message}")
        print("-------------")

        return True