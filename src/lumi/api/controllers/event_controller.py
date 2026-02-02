from fastapi import APIRouter
from lumi.infrastructure.event_bus.event_bus import event_bus

router = APIRouter()


@router.get("/events")
def listen_events():
    event = event_bus.wait_for_event()
    return event