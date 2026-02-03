from fastapi import APIRouter
from pydantic import BaseModel

from lumi.application.services.intent_router_service import IntentRouterService
from lumi.application.use_cases.process_user_input_use_case import ProcessUserInputUseCase
from lumi.application.dto.user_input_dto import UserInputDTO

router = APIRouter()
intent_router = IntentRouterService()

class ChatRequest(BaseModel):  
    message: str
    session_id : str | None = None 


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    dto = UserInputDTO(message=request.message, session_id = request.session_id)
    print(f"\nReceived message: {dto.message}\nsession_id: {dto.session_id}\ndto timestamp: {dto.timestamp}\n")

    process_user_input = ProcessUserInputUseCase()


    response = process_user_input.execute(dto)
    return ChatResponse(reply=response)