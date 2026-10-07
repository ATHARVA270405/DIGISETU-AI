class HumanApproval:

    def approve(self, message: str) -> bool:

        print("\n--- OUTREACH MESSAGE ---")
        print(message)
        print("------------------------")

        choice = input("Approve and send this message? (yes/no): ")

        return choice.strip().lower() == "yes"