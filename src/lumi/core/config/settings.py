from dataclasses import dataclass


@dataclass
class Settings:
    AI_MODEL : str = "gpt-4"
    AI_MAX_TOKENS : int = 1500
    STT_MODEL_SIZE : str = "base"
    TTS_MODEL_PATH : str = "./lumi/infrastructure/voice/voice_models/pt_BR-faber-medium.onnx"
    BASE_URL : str = "http://localhost:8000"