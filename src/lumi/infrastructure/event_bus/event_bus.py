from queue import Queue

class EventBus:
    def __init__(self):
        self.queue = Queue()

    def publish(self, event:dict):
        self.queue.put(event)
    
    def wait_for_event(self):
        return self.queue.get()

event_bus = EventBus()