import request
from lumi.core.config.settings import Settings

class WhatsAppService:

    def __init__(self):
        self.settings = Settings()

    
    def send_message(self, text:str):
        url = f"https://graph.facebook.com/v19.0/{self.settings.WHATSAPP_PHONE_NUMBER_ID}/messages"

        headers = {
            "Authorization" : f"" f"Bearer {self.settings.WHATSAPP_TOKEN}",
            "Content-Type" : "application/json"
        }

        payload = {
            "messaging_product" : "whatsapp",
            "to": self.settings.MY_PHONE_NUMBER,
            "type" : "text",
            "text" : {"body": text}
        }

        request.post(url, json=payload, headers=headers)