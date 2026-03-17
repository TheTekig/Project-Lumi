from google import genai
import os
from dotenv import load_dotenv


print("========================================")
import sounddevice as sd
print(sd.query_devices())
print("Dispositivos de Áudio Disponíveis:")
for idx, device in enumerate(sd.query_devices()):
    print(f"{idx}: {device['name']} - Input Channels: {device['max_input_channels']}, Output Channels: {device['max_output_channels']}")