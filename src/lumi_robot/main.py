from voice.stt_service import SpeechToTextService
from voice.tts_service import TextToSpeechService
from client.client import BackendClient
import threading
import time

def main():
    print("Lumi Inicializada")

    stt = SpeechToTextService()
    tts = TextToSpeechService()
    backend = BackendClient()

    event_thread = threading.Thread(
        target= event_listener,
        args=(backend, tts),
        daemon=True
    )

    event_thread.start()

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


def event_listener(backend, tts):
    print("Event Listener Iniciado")

    while True:
        try:
            event = backend.listen_events(timeout=10)
            if not event:
                continue

            print(f"Evento Recebido: {event}")

            if event["type"] == "TIMER_FINISHED":
                tts.speak(event["message"])

            elif event["type"] == "Alarm Reminder":
                tts.speak(event["message"])

            elif event["type"] == "AI_SYSTEM_REQUEST":
                tts.speak(event["message"])
        
        except Exception as e:
            print("Erro no event_listener", e)
            time.sleep(2)


if __name__ == "__main__":
    main()







