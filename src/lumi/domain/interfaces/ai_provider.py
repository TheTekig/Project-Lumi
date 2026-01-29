from abc import ABC, abstractmethod
from typing import Optional

class AIProvaider(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, max_tokens) -> Optional[str]:
        pass
    
