from google import genai
from google.genai import types
from dotenv import load_dotenv
from typing import Optional
import os

from lumi.core.config.settings import Settings
from lumi.domain.interfaces.ai_provider import AIProvaider

class GeminiProvider(AIProvaider):

    def __init__(self):
        self.settings = Settings()
        self.client = self.inicialize_gemini_client()
        self.model = self.settings.AI_GEMINI_MODEL
        self.max_tokens = self.settings.AI_MAX_TOKENS

    
    def inicialize_gemini_client(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("Error: GEMINI_API_KEY not found in environment variables.")
            return None
        return genai.Client(api_key=api_key)
        

    def generate_text(self, prompt: str, max_tokens) -> Optional[str]:
        try:
            print("Generating response from Gemini...")
            response = self.client.models.generate_content(
                model=self.model,
                config=types.GenerateContentConfig(
                    max_output_tokens=max_tokens,
                    temperature=0.6,
                    system_instruction=f"""Você é Lumi, uma assistente virtual inteligente projetada para ser uma assistente culinaria inteligente. 
        Responda de forma curta, clara, simpatica e objetiva."""
                ),
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            print(f"Error during Gemini completion: {e}")
            return None