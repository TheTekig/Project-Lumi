import requests
from core.settings import Settings

class BackendClient:
    def __init__(self):
        self.settings = Settings()
        self.base_url = self.settings.BASE_URL

    def send_command(self, text: str, session_id = "lumi-home"):
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={"message": text, "session_id": session_id}
        )
        return response.json()["reply"]
