class LeadLifecycleManager:

    def update_status(
        self,
        current_status: str,
        event: str,
    ) -> str:

        current_status = current_status.strip().upper()
        event = event.strip().upper()

        if event == "QUALIFIED":
            return "QUALIFIED"

        if event == "CONTACTED":
            return "CONTACTED"

        if event == "REPLIED":
            return "REPLIED"

        if event == "INTERESTED":
            return "INTERESTED"

        if event == "NOT_INTERESTED":
            return "LOST"

        if event == "CONVERTED":
            return "CONVERTED"

        return current_status