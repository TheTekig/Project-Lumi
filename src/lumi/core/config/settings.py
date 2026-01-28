from dataclasses import dataclass


@dataclass
class Settings:
    AI_MODEL : str = "gpt-4"
    AI_MAX_TOKENS : int = 1500