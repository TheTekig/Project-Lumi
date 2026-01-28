from lumi.infrastructure.ai.openai_provider import OpenAIClient

class AIProviderManager:
    def __init__(self):
        self.provider = [
            OpenAIClient()
        ]

    def generate(self, prompt: str) -> str:
        for provider in self.provider:
            response = provider.execute_ai_response(prompt, provider.max_tokens)
            if response:
                return response
        return "Error: No AI provider available."
        