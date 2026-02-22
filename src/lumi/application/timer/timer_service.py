import re
import threading
import time

from lumi.domain.entities.timer import Timer
from lumi.infrastructure.event_bus.event_bus import event_bus



class TimerService: #Responsavel pela criação e gerenciamento dos timer ativos

    def __init__(self):
        self.active_timers : dict[str,Timer] = {}


    def parse_time(self, message: str) -> int: #Extrai o tempo do timer do input do usuario
        
        message = message.lower()

        match = re.search(r'(\d+)\s*(segundos|seconds|sec|s|minutos|minutes|min|m|horas|hours|h)', message)
        
        if match:

            value = int(match.group(1))
            unit = match.group(2)

            if unit == 'segundos' or unit == 'seconds' or unit == 'sec' or unit == 's':
                return value
            elif unit == 'minutos' or unit == 'minutes' or unit == 'min' or unit == 'm':
                return value * 60
            elif unit == 'horas' or unit == 'hours' or unit == 'h':
                return value * 3600
        
        else:
            named_time = self.parse_named_time(message)
            if named_time > 0:
                return named_time

        return 0
    
    def parse_named_time(self, message: str) -> int: #Reponsavel por extrair o tempo do timer no input do usuario com base em formas comumente faladas de tempo
        message = message.lower()

        named_times = {
            "a few seconds": 5,
            "half a minute": 30,
            "a minute": 60,
            "five minutes": 300,
            "ten minutes": 600,
            "a quarter hour": 900,
            "half an hour": 1800,
            "an hour": 3600,
            "meia hora": 1800,
            "uma hora": 3600,
            "um minuto": 60
        }

        for name, seconds in named_times.items():
            if name in message:
                return seconds

        return 0
    
    def parse_timer_name(self, message: str) -> str: #Extrai o nome que dever ser direcionado ao timer
        message = message.lower()

        match = re.search(r'(?:timer|alarm|reminder|cronômetro|cronometro|alarme)\s+(?:para|pra|pro|do|da|de)\s+(.+?)(?:\s+(?:for|por|em|durante)|$)', message)
        
        if match:
            return match.group(1).strip()
        
        return ""

    def create_timer(self, name: str, duration_seconds: int, callback) -> Timer: #Cria uma instancia do objeto timer para rodar em um outra thread para não travar o backend
        timer = Timer.create(duration_seconds, name) #Cria uma instancio do objeto Timer
        self.active_timers[timer.id] = timer #Adiciona o timer como ativo no Active_timers utilizando seu id 

        thread = threading.Thread(target=self._run_timer, args=(timer, callback), daemon=True) #define a thread para o rodar, sendo o target o método que sera rodado na thread o args sendo os paramentro.
        thread.start()#Inicializa a Thread

        print(f"Timer:{timer.id}\nDuration: {timer.duration_seconds} seconds\nCreated: {timer.created_at}\nEnds: {timer.ends_at}\nStatus: {timer.active}.\n") #Print um mini log da ação que foi inicializada

        return timer


    def _run_timer(self, timer: Timer, callback): #Responsavel por rodar o timer

        total = timer.duration_seconds

        checkpoints = [] #Pontos de checkpoint para realizar notificações
        
        if total > 300:
            checkpoints.append(300)
        
        if total > 60:
            checkpoints.append(60)
        
        if total > 10:
            checkpoints.append(10)

        checkpoints.sort(reverse=True)

        remaining = total

        for checkpoint in checkpoints: #Passa checkpoin por checkpoint esperando o tempo corrento e notifica o checkpoint
            time.sleep(remaining - checkpoint)
            remaining = checkpoint
            self._notify_checkpoint(timer, remaining)

        time.sleep(remaining) # Faz ele esperar o tempo do checkpoint acabar
        event_bus.publish({ 
            "type": "TIMER_FINISHED",
            "message" : f"Alarme {timer.id} Finalizado" 
            }) #Manda o evento de Timer_Finished para a parte de Eventos para lumi falar
        
        callback(timer) # Faz o callback com a mensagem que o timer terminou

        del self.active_timers[timer.id] #deleta o timer da lista de timers ativos

    def _notify_checkpoint(self, timer: Timer, remaining_seconds: int):
        if remaining_seconds >= 60: # Verifica se falta mais de 1 minuto para formatação
            minutes = remaining_seconds // 60
            print(f"\nTimer: {timer.id} - {minutes} minute(s) remaining.")
            
            event_bus.publish({
                "type": "Alarm Reminder",
                "message": f"\nFaltam {minutes} minutos para o alarme {timer.id} terminar."
            }) #Manda o evento Alarm Reminder para a parte de eventos para lumi falar

        else:
            print(f"\nTimer: {timer.id} - {remaining_seconds} second(s) remaining.")
            
            event_bus.publish({
                "type": "Alarm Reminder",
                "message": f"\nFaltam {remaining_seconds} segundos para o alarme {timer.id} terminar."
            }) #Manda o evento Alarm Reminder para a parte de eventos para lumi falar