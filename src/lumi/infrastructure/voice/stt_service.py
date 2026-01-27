from faster_whisper import WhisperModel
from lumi.core.config.settings import Settings

class SpeechToTextService:
    def __init__(self):
        self.settings = Settings()
        self.model = WhisperModel(self.settings.STT_MODEL_SIZE)

        def transcribe(self, audio_path: str) -> str:
            segments, _ = self.model.transcribe(audio_path)

            text = ""
            for segment in segments:
                text += segment.text 
            
            return text


