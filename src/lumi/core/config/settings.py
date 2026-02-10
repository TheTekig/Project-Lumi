from dataclasses import dataclass
from dotenv import load_dotenv
import os



@dataclass
class Settings: #Configurações gerais - Modelos, Tokens e chaves de API

    load_dotenv()

    AI_GPT_MODEL : str = "gpt-4"
    AI_GEMINI_MODEL : str = "gemini-2.5-flash"
    AI_MAX_TOKENS : int = 1500

    GEMINI_API_KEY : str = os.getenv("GEMINI_API_KEY")
    OPENAI_API_KEY : str = os.getenv("OPENAI_API_KEY")

    WHATSAPP_PHONE_NUMBER_ID : str = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
    WHATSAPP_TOKEN: str = os.getenv("WHATSAPP_TOKEN")

    MY_PHONE_NUMBER : str = "5527999232026"
