from lumi.application.dto.user_input_dto import UserInputDTO
from lumi.application.use_cases.process_ia_input_use_case import ProcessIAInputCase
from lumi.application.use_cases.process_user_input_use_case import ProcessUserInputUseCase
from lumi.infrastructure.ai.provider_manager import AIProviderManager
from lumi.domain.enums.intent_type import IntentType

class ConversationOrchestrator:
    """Orchestrator passa para o processamento correto os inputs recebidos sendo encaixado como IA ou User"""
    def __init__(self): #Inicializa  outros módulos para processamento 
        self.user_uc = ProcessUserInputUseCase()
        self.ai_uc = ProcessIAInputCase(self.user_uc)
        self.ai_provider = AIProviderManager()

    def handle_user_message(self, dto): #Método responsavel por gerenciar qual rota sera pega para o input do usuario ou ia
        response = self.user_uc.execute(dto)

        if response == IntentType.FREE_CHAT:
            ai_text = self.ai_provider.generate(dto.message)
            return self.ai_uc.execute(ai_text, dto.session_id)
        
        return response
    
    """
    Foi necessario a implementação do ConversationOrchestrator para contornar um eventual problema de import circular,
    onde o ProcessUserInputUseCase importa o ProcessIAInputCase e o mesmo importa o ProcessUserInputUseCase!
      """