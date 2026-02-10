from voice.stt_service import SpeechToTextService
from voice.tts_service import TextToSpeechService
from client.client import BackendClient
from queue import Queue
import threading
import time

def main():
    print("Lumi Inicializada")

    stt = SpeechToTextService()
    tts = TextToSpeechService()
    backend = BackendClient()

    speech_queue = Queue()

    speech_thread = threading.Thread(
        target=speech_worker,
        args=(tts,speech_queue),
        daemon=True
    )

    speech_thread.start()

    event_thread = threading.Thread(
        target= event_listener,
        args=(backend, speech_queue),
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
            if not reply:
                print("Backend returns None")
            print(f"Reply : {reply}")

            speech_queue.put(reply)


def event_listener(backend, speech_queue):
    print("Event Listener Iniciado")

    while True:
        try:
            event = backend.listen_events(timeout=10)
            if not event:
                continue

            print(f"Evento Recebido: {event}")

            if event["type"] == "TIMER_FINISHED":
                speech_queue.put(event["message"])

            elif event["type"] == "Alarm Reminder":
                speech_queue.put(event["message"])

            elif event["type"] == "AI_SYSTEM_REQUEST":
                speech_queue.put(event["message"])
        
        except Exception as e:
            print("Erro no event_listener", e)
            time.sleep(2)

def speech_worker(tts, speech_queue):
    print("Speech worker iniciado")

    while True:
        text = speech_queue.get()
        try:
            tts.speak(text)
        
        except Exception as e:
            print("Erro no TTS", e)
        
        finally:
            speech_queue.task_done()


if __name__ == "__main__":
    main()







