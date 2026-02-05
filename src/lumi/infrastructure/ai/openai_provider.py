from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional
import os

from lumi.core.config.settings import Settings
from lumi.domain.interfaces.ai_provider import AIProvaider

class OpenAIClient(AIProvaider):
    
    def __init__(self):
        self.settings = Settings()
        self.client = self.inicialize_openai_client()
        self.model = self.settings.AI_GPT_MODEL
        self.max_tokens = self.settings.AI_MAX_TOKENS

    def inicialize_openai_client(self) -> OpenAI:
    
        api_key = self.settings.OPENAI_API_KEY

        if not api_key:
            print("Error: OPENAI_API_KEY not found in environment variables.")
            return None

        try:
            return OpenAI(api_key=api_key)
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            return None
    
    def generate_text(self, prompt: str, max_tokens) -> Optional[str]:
        try:
            print("Generating response from OpenAI...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": f"""

                     - Você é Lumi, uma assistente virtual inteligente projetada para ser uma assistente culinaria inteligente. 
                     - Responda de forma curta, clara, simpatica e objetiva.
                     - Sempre que você decidir tomar uma ação pelo usuario (como colocar alarmes, começar receitas, mover para o proxímo passo), você DEVE incluir a marcação correspondente no final da sentença: 

                      *[CREATE_TIMER] - Utilize essa marcação caso queira deixar um alarme, ou uma mensagem programada para o usuario;
                      *[CREATE_RECIPE] - Utilize essa marcação para criação de alguma receita;
                      *[NEXT_STEP] - Utilize essa marcação que achar que o usuario esta preparado para o próximo passo da receita;
                      *[START_RECIPE] - Utilize essa marcação quando quiser iniciar uma receita;
                     
                     - NUNCA EXPLIQUE AS TAGS
                     - NUNCA COLOQUE AS TAGS NO MEIO DA SENTENÇA
                     - SEMPRE COLOQUE AS TAGS NO FINAL DA SENTENÇA
                     
                      """},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.6
            )
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Error during OpenAI completion: {e}")
            return None

    
    