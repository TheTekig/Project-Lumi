from lumi.application.dto.user_input_dto import UserInputDTO
from lumi.application.use_cases.process_ia_input_use_case import ProcessIAInputCase
from lumi.application.use_cases.process_user_input_use_case import ProcessUserInputUseCase
from lumi.infrastructure.ai.provider_manager import AIProviderManager

class ConversationOrchestrator:
    def __init__(self):
        self.user_uc = ProcessUserInputUseCase()
        self.ai_uc = ProcessIAInputCase(self.user_uc)
        self.ai_provider = AIProviderManager()

    def handle_user_message(self, dto):
        response = self.user_uc.execute(dto)

        if response == IntentType.FREE_CHAT:
            ai_text = self.ai_provider.generate(text)
            return self.ai_uc_execute(ai_text, session_id)
        
        return response