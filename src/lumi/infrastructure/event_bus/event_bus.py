from queue import Queue, Empty

class EventBus: #Faz o envio dos eventos para Lumi-Robot - Lista eventos
    def __init__(self):
        self.queue = Queue()

    def publish(self, event:dict):
        print("Publishing Event: ", event)
        self.queue.put(event)
    
    def wait_for_event(self, timeout=60):
        try:
            return self.queue.get(timeout=timeout)
        except Empty:
            return None

event_bus = EventBus()