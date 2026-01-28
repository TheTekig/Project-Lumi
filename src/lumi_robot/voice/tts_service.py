import subprocess
import uuid
import os

from lumi_robot.core.settings import Settings
import sounddevice as sd
from scipy.io.wavfile import read

class TextToSpeechService:
    def __init__(self):
        self.settings = Settings()
        self.model_path = self.settings.TTS_MODEL_PATH

    def speak(self, text: str):

        filename = f"tts_{uuid.uuid4()}.wav"

        self.generate_audio(text, filename)
        self.play_audio(filename)
        os.remove(filename)

    def generate_audio(self, text:str, output_file:str):

        command = [
            "piper",
            "--model", self.settings.TTS_MODEL_PATH,
            "--output_file", output_file
        ]

        subprocess.run(
            command,
            input=text.encode("utf-8"),
            stdout = subprocess.DEVNULL,
            stdeer = subprocess.DEVULL
        )

    def play_audio(self, audio_file: str):

        fs, audio = read(audio_file)

        sd.play(audio, fs, device=self.settings.AUDIO_DEVICE)
        sd.wait()
       