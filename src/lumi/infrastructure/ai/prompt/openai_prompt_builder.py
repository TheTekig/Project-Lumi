from dataclasses import dataclass

@dataclass
class promptBuilder:

    @staticmethod
    def build_prompt(task: str, context: str) -> str:
        prompt = f"Task: {task}\n\nContext: {context}\n\nPlease provide a detailed response based on the above task and context."

    def chat_prompt(user_text: str) -> str:
        return f"""
        Você é Lumi, uma assistente virtual inteligente projetada para ser uma assistente culinaria inteligente. 
        Responda de forma curta, clara, simpatica e objetiva.
        Usuario: {user_text}
        """