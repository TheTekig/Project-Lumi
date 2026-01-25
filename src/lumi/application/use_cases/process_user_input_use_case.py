from lumi.application.services.timer_service import TimerService
from lumi.application.services.intent_router_service import IntentRouterService, IntentType
from lumi.application.dto.user_input_dto import UserInputDTO

class ProcessUserInputUseCase:

    def __init__(self):
        self.intent_router = IntentRouterService()
        self.timer_service = TimerService()

    def execute(self, user_input_dto: UserInputDTO) -> str:
        user_text = user_input_dto.lower()

        intent = self.intent_router.detect(user_text)

        if intent == IntentType.GREETING:
            return "Hello! How can I assist you today?"

        if intent == IntentType.RECIPE_REQUEST:
            return "I can help you with recipes. What would you like to cook?"

        if intent == IntentType.TIMER_CREATE:
            duration_seconds = self.timer_service.parse_time(user_text)
            parsed_timer_name = self.timer_service.parse_timer_name(user_text)

            if duration_seconds > 0:
                self.timer_service.create_timer(parsed_timer_name, duration_seconds, lambda timer: print(f"Timer {timer.id} ended."))

                return f"Timer set for {duration_seconds} seconds."

            else: 
                return f"Could you please specify the duration for the timer?"

        return f"You said: {user_text}"
