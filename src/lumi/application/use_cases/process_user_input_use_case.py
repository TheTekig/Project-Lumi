from lumi.application.services.timer_service import TimerService
from lumi.application.services.intent_router_service import IntentRouterService, IntentType
from lumi.application.dto.user_input_dto import UserInputDTO
from lumi.application.services.conversation_session_manager import ConversationSessionManager
from lumi.application.services.recipe_service import RecipeService
from lumi.infrastructure.database.recipe_repository import RecipeRepository

class ProcessUserInputUseCase:

    def __init__(self):
        self.intent_router = IntentRouterService()
        self.timer_service = TimerService()
        self.session_manager = ConversationSessionManager()
        self.recipe_service = RecipeService()

    def execute(self, user_input_dto: UserInputDTO) -> str:
        user_text = user_input_dto.message.lower()
        intent = self.intent_router.detect(user_text)

        session = self.session_manager.get_or_create(user_input_dto.session_id)
        session.last_message = user_input_dto.message
        session.last_intent = intent

        if intent == IntentType.GREETING:
            return "Hello! How can I assist you today?"

        if intent == IntentType.RECIPE_REQUEST:
            recipe_session = self.recipe_service.get_recipe(user_text)
            if not recipe_session:
                recipes = self.recipe_service.list_recipes()
                recipe_names = ', '.join([recipe.name for recipe in recipes])
                return f"Sorry, I couldn't find that recipe. Here are some recipes you can try: {recipe_names}."
            
            session.current_recipe = recipe_session
            first_step = recipe_session.steps[0]

            return "I can help you with recipes. What would you like to cook?"

        if intent == IntentType.TIMER_CREATE:
            duration_seconds = self.timer_service.parse_time(user_text)
            parsed_timer_name = self.timer_service.parse_timer_name(user_text)

            if duration_seconds > 0:
                self.timer_service.create_timer(parsed_timer_name, duration_seconds, lambda timer: print(f"Timer {timer.id} ended."))

                return f"Timer set for {duration_seconds} seconds."

            else: 
                return f"Could you please specify the duration for the timer?"
        
        if intent == IntentType.CONFIRMATION and session.current_recipe:
            step = session.current_step

            if session.current_step < len(session.current_recipe.steps):
                return f"Great! Next step: {session.current_recipe.steps[session.current_step]}"
            
            
            session.current_recipe = None
            session.current_step = 0
            return "You've completed the recipe! Enjoy your meal."

        if intent == IntentType.FREE_CHAT:
            pass

        return f"You said: {user_text}"
