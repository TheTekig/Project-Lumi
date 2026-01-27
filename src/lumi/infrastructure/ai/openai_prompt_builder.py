from dataclasses import dataclass

@dataclass
class promptBuilder:
    @staticmethod
    def build_prompt(task: str, context: str) -> str:
        prompt = f"Task: {task}\n\nContext: {context}\n\nPlease provide a detailed response based on the above task and context."
        return prompt