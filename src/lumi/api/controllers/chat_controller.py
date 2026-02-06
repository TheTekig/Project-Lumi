from fastapi import APIRouter
from pydantic import BaseModel

from lumi.application.intent.intent_router_service import IntentRouterService
from lumi.application.dto.user_input_dto import UserInputDTO
from lumi.application.orchestrators.conversation_orchestrator import ConversationOrchestrator
router = APIRouter()
intent_router = IntentRouterService()
orchestrator = ConversationOrchestrator()

class ChatRequest(BaseModel):  
    message: str
    session_id : str | None = None 


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    dto = UserInputDTO(message=request.message, session_id = request.session_id)
    print(f"\nReceived message: {dto.message}\nsession_id: {dto.session_id}\ndto source: {dto.source}\ndto timestamp: {dto.timestamp}\n")

    response = orchestrator.handle_user_message(dto)

    return ChatResponse(reply=response)