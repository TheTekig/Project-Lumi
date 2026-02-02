from fastapi import FastAPI

from lumi.api.controllers.chat_controller import router as chat_router
from lumi.api.controllers.health_controller import router as health_router
from lumi.api.controllers.event_controller import router as event_router

app = FastAPI(title="Project LUMI")

app.include_router(chat_router, prefix="/api")
app.include_router(event_router, prefix="/api")
app.include_router(health_router) 
