from fastapi import APIRouter
from lumi.infrastructure.event_bus.event_bus import event_bus

router = APIRouter()


@router.get("/events")
def listen_events():
    event = event_bus.wait_for_event(timeout=60)

    if event:
        print("Sending Event: ", event)
        return event

    print("Sending Event: ", event)
    return {}