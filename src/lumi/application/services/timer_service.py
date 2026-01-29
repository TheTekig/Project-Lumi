import re
import threading
import time

from lumi.domain.entities.timer import Timer

class TimerService:

    def __init__(self):
        self.active_timers : dict[str,Timer] = {}

    def parse_time(self, message: str) -> int:
        
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
    
    def parse_named_time(self, message: str) -> int:
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
    
    def parse_timer_name(self, message: str) -> str:
        message = message.lower()

        match = re.search(r'(?:timer|alarm|reminder|cronômetro|cronometro|alarme)\s+(?:para|pra|pro|do|da|de)\s+(.+?)(?:\s+(?:for|por|em|durante)|$)', message)
        
        if match:
            return match.group(1).strip()
        
        return "Unnamed Timer"

    def create_timer(self, name: str, duration_seconds: int, callback) -> Timer:
        timer = Timer.create(duration_seconds, name)
        self.active_timers[timer.id] = timer

        thread = threading.Thread(target=self._run_timer, args=(timer, callback), daemon=True)
        thread.start()

        print(f"Timer:{timer.id}\nDuration: {timer.duration_seconds} seconds\nCreated: {timer.created_at}\nEnds: {timer.ends_at}\nStatus: {timer.active}.\n")

        return timer


    def _run_timer(self, timer: Timer, callback):

        total = timer.duration_seconds

        checkpoints = []
        
        if total > 300:
            checkpoints.append(300)
        
        if total > 60:
            checkpoints.append(60)
        
        if total > 10:
            checkpoints.append(10)

        checkpoints.sort(reverse=True)

        remaining = total

        for checkpoint in checkpoints:
            time.sleep(remaining - checkpoint)
            remaining = checkpoint
            self._notify_checkpoint(timer, remaining)

        time.sleep(remaining)
        callback(timer)

        del self.active_timers[timer.id]

    def _notify_checkpoint(self, timer: Timer, remaining_seconds: int):
        if remaining_seconds >= 60:
            minutes = remaining_seconds // 60
            print(f"\nTimer: {timer.id} - {minutes} minute(s) remaining.")
        else:
            print(f"\nTimer: {timer.id} - {remaining_seconds} second(s) remaining.")