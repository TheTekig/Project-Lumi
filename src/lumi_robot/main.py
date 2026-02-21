from voice.stt_service import SpeechToTextService
from voice.tts_service import TextToSpeechService
from client.client import BackendClient
from display.emotion_display import EmotionDisplayService
import threading
import time
import torch




def main():
    print("Lumi Inicializada")
    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0))



    stt = SpeechToTextService()
    tts = TextToSpeechService()
    backend = BackendClient()


    tts.speak("Lumi Inicialized! just waiting for the wake word")

    while True:
        
        print("Lumi Esperando por Wake-Word")
        

        if stt.wait_for_wake_word():

            print("Lumi Ativa. Ouvindo comando...")
            transciption = stt.listen_command()
            print(f"command : {transciption}")

            if not transciption:
                print("None")
                continue
            
            reply = backend.send_command(transciption)
            print(f"Reply : {reply}")

            
            tts.speak(reply)
            time.sleep(1)
        """
        event = backend.listen_events()
        if not event:
            continue
        if event["type"] == "TIMER_FINISHED":
            tts.speak(event["message"])
        if event["type"] == "Alarm Reminder":
            tts.speak(event["message"])
        if event["type"] == "AI-System Request":
            tts.speak(event["message"])
            """


def event_listener(backend: BackendClient, tts: TextToSpeechService):
    print("Iniciando Event Listener...")
    while True:
        try: 

            event = backend.listen_events(timeout=10)
            if not event:
                continue

            print(f"Evento recebido: {event}")
            if event["type"] == "TIMER_FINISHED":
                tts.speak(event["message"])
            if event["type"] == "Alarm Reminder":
                tts.speak(event["message"])
            if event["type"] == "AI-System Request":
                tts.speak(event["message"])
        
        except Exception as e:
            print(f"Erro ao ouvir eventos: {e}")
            time.sleep(5)  # Espera antes de tentar novamente

        finally:
            print("Event Listener finalizado.")

if __name__ == "__main__":
    main()







