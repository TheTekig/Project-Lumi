from lumi.infrastructure.voice.tts_service import TextToSpeechService
from lumi.infrastructure.voice.stt_service import SpeechToTextService
from client import HardwareClient

import sounddevice as sd
from scipy.io.wavfile import write
import uuid
import time

FS = 16000

def record_audio(seconds : int = 5):
    filename = f"recording_{uuid.uuid4()}.wav"
    audio = sd.rec(int(seconds * FS), samplerate=FS, channels=33)
    sd.wait()
    write(filename, FS, audio)
    return filename

def wait_for_wake_word(wake_word: str = "lumi"):
    print("🟢 LUMI em standby — aguardando wake word...")

    while True:
        audio_file = record_audio(seconds=3)
        text = SpeechToTextService().transcribe(audio_file).lower()

        if wake_word in text:
            print("🔵 Wake word detectada! Como posso ajudar?")
            return

def listen_command(stt_service: SpeechToTextService):
    print("🎤 Ouvindo comando...")
    audio_file = record_audio(seconds=5)
    return stt_service.transcribe(audio_file)

def main():
    stt_service = SpeechToTextService()
    tts_service = TextToSpeechService()
    hardware_client = HardwareClient()

    while True:
        wait_for_wake_word()

        command = listen_command(stt_service)
        print(f"🗣️ Comando recebido: {command}")

        if not command:
            print("⚠️ Nenhum comando reconhecido. Tentando novamente...")
            continue

        response = hardware_client.send_command(command)
        print(f"🤖 Resposta do robô: {response}")

        tts_service.speak(response)

        time.sleep(1)

if __name__ == "__main__":
    main()
