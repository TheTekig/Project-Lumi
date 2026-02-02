import subprocess
import uuid
import os
import wave

from piper import PiperVoice , SynthesisConfig

from pathlib import Path
from core.settings import Settings

import sounddevice as sd
from scipy.io.wavfile import read

class TextToSpeechService:
    def __init__(self):
        self.settings = Settings()
        self.model_path = self.settings.TTS_MODEL_PATH



    def speak(self, text: str):

        filename = f"./src/lumi_robot/voice/temp/tts_{uuid.uuid4()}.wav"

        self.generate_audio(text, str(filename))

        self.play_audio(filename)
        os.remove(filename)

    def generate_audio(self, text:str, output_file:str):
        
        syn_config = SynthesisConfig(
            volume=0.5, 
            length_scale=0.6, 
            noise_scale=1.0, 
            noise_w_scale=1.0, 
            normalize_audio=False, 
        )

        voice = PiperVoice.load(Path(self.model_path))
        with wave.open(output_file, "wb") as wf:
            voice.synthesize_wav(text, wf, syn_config)
        

    def play_audio(self, audio_file: str):

        fs, audio = read(audio_file)
        sd.play(audio, fs, device=self.settings.AUDIO_DEVICE)
        sd.wait()
       