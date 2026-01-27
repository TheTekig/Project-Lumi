import subprocess
import uuid

from lumi.core.config.settings import Settings

class TextoToSpeechService:
    def __init__(self):
        self.settings = Settings()
        self.model_path = self.settings.TTS_MODEL_PATH

    def speak(self, text: str) -> str:
        output_filename = f"tts_output_{uuid.uuid4()}.wav"
        
        command = [
            "piper",
            "--model", self.model_path,
            "--output_file", output_filename,
        ]

        process = subprocess.Popen(command, stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))

        subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filename])