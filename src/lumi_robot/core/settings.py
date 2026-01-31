from dataclasses import dataclass

@dataclass
class Settings:

    voice_models = [{
        "name": "Faber",
        "path": "./src/lumi_robot/voice/voice_models/pt_BR-faber-medium.onnx",
        "language": "pt-BR",
    },
    {
        "name": "Amy",
        "path": "./src/lumi_robot/voice/voice_models/en_us-amy-medium.onnx",
        "language": "en-US",
    }
    ]

    PIPER_PATH: str = "./src/lumi_robot/voice/voice_models/piper/piper.exe"
    TTS_MODEL_PATH: str = "./src/lumi_robot/voice/voice_models/en_us-amy-medium.onnx"
    STT_MODEL_SIZE: str = "base"
    BASE_URL : str = "http://localhost:8000"
    FS: int = 48000
    AUDIO_DEVICE: int = 1
    MICROPHONE_DEVICE: int = 11
    LUMI_WAKE_WORD: str = "lumi"
