import re
import threading
import time

from lumi.domain.entities.timer import Timer

class TimerService:

    def __init__(self):
        self.active_timers : dict[str,Timer] = {}

    def parse_time(self, message: str) -> int:
        
        message = message.lower()

        match = re.search(r'(\d+)\s*(seconds|sec|s|minutes|min|m|hours|h)', message)
        
        if match:

            value = int(match.group(1))
            unit = match.group(2)

            if unit == 'seconds' or unit == 'sec' or unit == 's':
                return value
            elif unit == 'minutes' or unit == 'min' or unit == 'm':
                return value * 60
            elif unit == 'hours' or unit == 'h':
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
            "an hour": 3600
        }

        for name, seconds in named_times.items():
            if name in message:
                return seconds

        return 0
    
    def parse_timer_name(self, message: str) -> str:
        message = message.lower()

        match = re.search(r'timer for (.+?)(?: for|$)', message)
        
        if match:
            return match.group(1).strip()
        
        return "Unnamed Timer"

    def create_timer(self, name: str, duration_seconds: int, callback) -> Timer:

        timer = Timer.create(duration_seconds, name)
        self.active_timers[timer.id] = timer

        thread = threading.Thread(target=self._run_timer, args=(timer, callback))
        thread.start()

        return timer


    def _run_timer(self, timer: Timer, callback):
        time.sleep(timer.duration_seconds)

        timer.active = False
        callback(timer)

        del self.active_timers[timer.id]