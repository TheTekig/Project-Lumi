from voice.stt_service import SpeechToTextService
from voice.tts_service import TextToSpeechService
from client.client import BackendClient
import time

def main():
    print("Lumi Inicializada")

    stt = SpeechToTextService()
    tts = TextToSpeechService()
    backend = BackendClient()

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

        event = backend.listen_events()
        if not event:
            continue
        if event["type"] == "TIMER_FINISHED":
            tts.speak(event["message"])
        if event["type"] == "Alarm Reminder":
            tts.speak(event["message"])


if __name__ == "__main__":
    main()







