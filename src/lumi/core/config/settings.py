from dataclasses import dataclass


@dataclass
class Settings:
    AI_GPT_MODEL : str = "gpt-4"
    AI_GEMINI_MODEL : str = "gemini-2.5-flash"
    AI_MAX_TOKENS : int = 1500