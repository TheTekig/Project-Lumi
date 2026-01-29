from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Erro: Sem API Key no .env")
else:
    client = genai.Client(api_key=api_key)
    print("=== MODELOS DISPONÍVEIS NA SUA CONTA ===")
    try:
        # Lista os modelos
        for model in client.models.list():
            # Mostra apenas o nome limpo (ex: gemini-1.5-flash)
            clean_name = model.name.replace("models/", "") 
            print(f"Nome para por no settings: {clean_name}")
    except Exception as e:
        print(f"Erro ao listar: {e}")