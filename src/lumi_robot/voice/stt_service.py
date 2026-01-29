from faster_whisper import WhisperModel
from lumi.core.config.settings import Settings

from scipy.io.wavfile import write
import sounddevice as sd
import uuid
import time

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
    
    def record_audio(self, seconds : int = 5) -> str:
        FS = self.settings.FS
        filename = f"recording_{uuid.uuid4()}.wav"
        audio = sd.rec(int(seconds * FS), samplerate= FS, channels=1, device= self.settings.MICROPHONE_DEVICE)
        sd.wait()
        write(filename, FS, audio)
        return filename
    
    def wait_for_wake_word(self, wake_word: str | None=None) -> bool:
        wake_word = self.settings.LUMI_WAKE_WORD or wake_word
        audio_file = self.record_audio(seconds = 3)
        text = self.transcribe(audio_file).lower()

        if wake_word in text:
            print("Wake word detected!")

            return True
    
    def listen_command(self) -> str:
        print("Ouvindo Comando...")
        audio_file = self.record_audio(seconds = 5)

        return self.transcribe(audio_file)

        


