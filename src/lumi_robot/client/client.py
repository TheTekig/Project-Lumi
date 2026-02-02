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

    def listen_events(self):
        try:
            response = requests.get(f"{self.base_url}/api/events", timeout=60)
            if response.status_code == 200:
                return response.json()
        
        except requests.exceptions.Timeout:
            return None
        except Exception as e:
            print(f"Erro ao escutar eventos: {e}")
            return None
        
