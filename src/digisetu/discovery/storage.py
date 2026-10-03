import json
from pathlib import Path


class LeadStorage:

    def __init__(self, file_path: str = "leads.json"):
        self.file_path = Path(file_path)

    def save(self, lead: dict[str, str]) -> None:
        leads = []

        if self.file_path.exists():
            with open(self.file_path, "r", encoding="utf-8") as file:
                leads = json.load(file)

        leads.append(lead)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(leads, file, indent=4)