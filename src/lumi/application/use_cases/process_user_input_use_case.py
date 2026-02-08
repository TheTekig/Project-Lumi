from lumi.application.timer.timer_service import TimerService
from lumi.application.intent.intent_router_service import IntentRouterService, IntentType
from lumi.application.dto.user_input_dto import UserInputDTO
from lumi.application.services.whatsapp_service import WhatsAppService
from lumi.application.recipe.recipe_flow import RecipeFlowService
from lumi.infrastructure.singletons import session_manager

class ProcessUserInputUseCase:

    def __init__(self):
        self.intent_router = IntentRouterService()
        self.timer_service = TimerService()
        self.session_manager = session_manager
        self.recipe_flow_service = RecipeFlowService()
        self.whatsapp_service = WhatsAppService()

    def execute(self, user_input_dto: UserInputDTO) -> str: 

        """Metodo responsavel pelo processamento do input do Usuario, ele trata o input e devolve"""
        print(f"\nReceived message: {user_input_dto.message}\nsession_id: {user_input_dto.session_id}\ndto source: {user_input_dto.source}\ndto timestamp: {user_input_dto.timestamp}\n")

        user_text = user_input_dto.message.lower()
        intent = self.intent_router.detect(user_text)

        session = self.session_manager.get_or_create(user_input_dto.session_id)    

        session.last_message = user_input_dto.message
        session.last_intent = intent

        match intent: #Parte Responsavel por chamar o metodo de cada IntentType retornando a resposta para Lumi
            
            case IntentType.GREETING:
                print("Status: Greeting intent detected.\n")
                return self.greeting(user_text = user_text)

            case IntentType.TIMER_CREATE:
                print("Status: Timer creation intent detected.\n")
                return self.timer_create(user_text = user_text)

            case IntentType.FREE_CHAT:
                print("Status: Free chat intent detected.\n")
                return intent

            case IntentType.MANAGE_RECIPE:
                print("Status: Manage recipe intent detected.\n")
                if user_input_dto.source == "ai":
                    return ""
                response = self.recipe_flow_service.manage_recipe(session, user_text)
                return response

            case _:
                return self.unknown_intent(user_text = user_text)

    def greeting(self, user_text: str) -> str:
        return "Hello! How can I assist you today?"
    
    def timer_create(self, user_text: str) -> str:
        duration_seconds = self.timer_service.parse_time(user_text)
        parsed_timer_name = self.timer_service.parse_timer_name(user_text)

        if duration_seconds > 0:
            self.timer_service.create_timer(parsed_timer_name, duration_seconds, lambda timer: print(f"Timer: {timer.id} - ended."))

            return f"Timer set for {duration_seconds} seconds."

        else: 
            return f"Could you please specify the duration for the timer?"
    
    def unknown_intent(self, user_text: str) -> str:
        return "I'm not sure how to help with that. Could you please rephrase?"
    