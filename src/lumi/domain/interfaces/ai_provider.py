from abc import ABC, abstractmethod

class AIProvaider(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass


    