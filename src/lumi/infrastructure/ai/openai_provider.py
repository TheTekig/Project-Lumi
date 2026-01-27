from openai import OpenAi
from dotenv import load_dotenv
from typing import Optional

from lumi.core.config.settings import Settings


class OpenAIClient:
    def __init__(self):
        self.settings = Settings()
        self.client = inicialize_openai_client()
        self.model = self.settings.AI_MODEL
        self.max_tokens = self.settings.AI_MAX_TOKENS

    def inicialize_openai_client(self) -> OpenAi:
        load_dotenv("venv/.env")
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            print("Error: OPENAI_API_KEY not found in environment variables.")
            return None

        try:
            return OpenAi(api_key=api_key)
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            return None
    
    def execute_ai_response(self, prompt: str, max_tokens) -> Optional[str]:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"Error during OpenAI completion: {e}")
            return None

    
    