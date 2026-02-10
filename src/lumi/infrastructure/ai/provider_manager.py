from lumi.infrastructure.ai.openai_provider import OpenAIClient
from lumi.infrastructure.ai.gemini_provider import GeminiProvider

class AIProviderManager: #Gerenciador dos provedores de IA
    def __init__(self):
        self.provider = [
            OpenAIClient(),
            GeminiProvider()
        ] #Fallback de IA's caso uma acabe os tokens ou ocorre erro de conexão a mesma recorre a proxima

    def generate(self, prompt: str) -> str:
        for provider in self.provider:
            response = provider.generate_text(prompt, provider.max_tokens)
            if response:
                return response
        
        print(response)
        return print("Error: No AI provider available.")
        