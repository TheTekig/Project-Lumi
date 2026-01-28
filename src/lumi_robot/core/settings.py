from dataclasses import dataclass

@dataclass
class Settings:
    TTS_MODEL_PATH: str = "./lumi_robot/voice/voice_models/pt_BR-faber-medium.onnx"
    STT_MODEL_SIZE: str = "base"
    BASE_URL : str = "http://localhost:8000"
    FS: int = 16000
    AUDIO_DEVICE: int | None = None
    MICROPHONE_DEVICE: int | None = None
    LUMI_WAKE_WORD: str = "lumi"
