from lumi.application.services.timer_service import TimerService
from lumi.application.services.intent_router_service import IntentRouterService, IntentType
from lumi.application.dto.user_input_dto import UserInputDTO
from lumi.application.services.conversation_session_manager import ConversationSessionManager
from lumi.application.services.recipe_service import RecipeService
from lumi.application.use_cases.process_ia_input_use_case import ProcessIAInputCase
from lumi.application.services.whatsapp_service import WhatsAppService
from lumi.application.services.recipe_flow import recipeFlowService
from lumi.infrastructure.ai.provider_manager import AIProviderManager
from lumi.infrastructure.singletons import session_manager

class ProcessUserInputUseCase:

    def __init__(self):
        self.intent_router = IntentRouterService()
        self.timer_service = TimerService()
        self.session_manager = session_manager
        self.recipe_service = RecipeService()
        self.recipe_flow_service = recipeFlowService()
        self.process_ia = ProcessIAInputCase()
        self.whatsapp_service = WhatsAppService()

    def execute(self, user_input_dto: UserInputDTO) -> str: 

        """Metodo responsavel pelo processamento do input do Usuario, ele trata o input e devolve"""

        user_text = user_input_dto.message.lower()
        intent = self.intent_router.detect(user_text)

        session = self.session_manager.get_or_create(user_input_dto.session_id)
        session.last_message = user_input_dto.message
        session.last_intent = intent

        match intent: #Parte Responsavel por chamar o metodo de cada IntentType retornando a resposta para Lumi
            
            case IntentType.GREETING:
                print("Status: Greeting intent detected.\n")
                return self.greeting(user_text = user_text)

            case IntentType.RECIPE_REQUEST:
                print("Status: Recipe request intent detected.\n")
                return self.recipe_request(session, user_text = user_text)

            case IntentType.TIMER_CREATE:
                print("Status: Timer creation intent detected.\n")
                return self.timer_create(user_text = user_text)

            case IntentType.FREE_CHAT:
                print("Status: Free chat intent detected.\n")
                return self.free_chat(user_text = user_text)
        
            case IntentType.SMALL_TALK:
                print("Status: Small talk intent detected.\n")
                return self.small_talk(user_text = user_text)

            case IntentType.IMAGE_ANALYSIS:
                print("Status: Image analysis intent detected.\n")
                return self.image_analysis(user_text = user_text)

            case IntentType.RECIPE_SUGESTION:
                print("Status: Recipe suggestion intent detected.\n")
                return self.recipe_suggestion(user_text = user_text)

            case IntentType.CONFIRMATION:
                print("Status: Step confirm")
                return self.confirm_step(session)
            
            case IntentType.RECIPE_DETAILS:
                print("Status: Recipe details intent detected.\n")
                session_recipe = session.current_recipe
                if not session_recipe or not session_recipe.active:
                    return "Não há nenhuma receita em andamento"
                ingredients =  session_recipe.list_ingredients()
                self.whatsapp_service.send_message(ingredients)
                return "Ingredients have been sent to your WhatsApp."

            case IntentType.MANAGE_RECIPE:
                print("Status: Manage recipe intent detected.\n")
                return self.manage_recipe(session, user_text)
            
            case _:
                return self.unknown_intent(user_text = user_text)

    
    def manage_recipe(self, session, user_text: str) -> str:
        
        if not session.current_recipe or not session.current_recipe.active:
            return "Não há nenhuma receita em andamento"
        
        else:
            if any(word in user_text for word in [
                "next step", "next", "próximo passo", "próximo", "seguinte",
                ]):
                recipe_session = session.current_recipe
                if not recipe_session or not recipe_session.active:
                    return "Não há nenhuma receita em andamento"
                
                next_step = recipe_session.next_step()
                print(next_step)
                if not next_step:
                    session.current_recipe = None
                    return "Receita Finalizada"
            
                return next_step
            if any(word in user_text for word in [
                "previous step", "previous", "passo anterior", "anterior",
                ]):
                recipe_session = session.current_recipe
                if not recipe_session or not recipe_session.active:
                    return "Não há nenhuma receita em andamento"
                
                previous_step = recipe_session.previus_step()
                print(previous_step)
            
                return previous_step
            if any(word in user_text for word in [
                "actual step", "execute step", "execute", "atual passo", "atual", "repeat step", "repeat", "repita passo", "repita",
                ]):
                recipe_session = session.current_recipe
                if not recipe_session or not recipe_session.active:
                    return "Não há nenhuma receita em andamento"
                
                actual_step = recipe_session.get_current_step()
                print(actual_step)
            
                return actual_step
            if any(word in user_text for word in [
                "list ingredients", "ingredients", "lista de ingredientes", "ingredientes",
                ]):
                recipe_session = session.current_recipe
                if not recipe_session or not recipe_session.active:
                    return "Não há nenhuma receita em andamento"
                
                ingredients = recipe_session.list_ingredients()
                print(ingredients)
            
                return ingredients
            
            if any(word in user_text for word in [
                "whatsapp", "analyze image", "analisar imagem",
                ]):
                return "not implemented yet" 
        
        
        
        pass

    def greeting(self, user_text: str) -> str:
        return "Hello! How can I assist you today?"

    def recipe_request(self, session, user_text: str) -> str:
        
        recipe_session = self.recipe_service.create_recipe_session(user_text)
        
        if not recipe_session:
            return "Receita não encontrada"
        
        session.current_recipe = recipe_session
        recipe_description = session.current_recipe.get_recipe_description()
        return recipe_description + "Lets Start?"   
    
    def timer_create(self, user_text: str) -> str:
        duration_seconds = self.timer_service.parse_time(user_text)
        parsed_timer_name = self.timer_service.parse_timer_name(user_text)

        if duration_seconds > 0:
            self.timer_service.create_timer(parsed_timer_name, duration_seconds, lambda timer: print(f"Timer: {timer.id} - ended."))

            return f"Timer set for {duration_seconds} seconds."

        else: 
            return f"Could you please specify the duration for the timer?"
        
    def confirm_step(self, session) -> str:
        recipe_session = session.current_recipe
        if not recipe_session or not recipe_session.active:
            return "Não há nenhuma receita em andamento"
        
        next_step = recipe_session.next_step()
        print(next_step)
        if not next_step:
            session.current_recipe = None
            return "Receita Finalizada"
    
        return next_step
    
    def free_chat(self, user_text: str) -> str:
        ai_provider_manager = AIProviderManager()
        response = ai_provider_manager.generate(prompt=user_text)
        if response:

            return response
        
        return "Sorry, I couldn't process your request at the moment."
    
    def small_talk(self, user_text: str) -> str:
        return "I'm here to chat! How's your day going?"
    
    def image_analysis(self, user_text: str) -> str:
        return "Please upload an image for analysis."
    
    def recipe_suggestion(self, user_text: str) -> str:
        recipes = self.recipe_service.list_recipes()
        recipe_names = ', '.join([recipe.name for recipe in recipes])
        return f"Here are some recipe suggestions: {recipe_names}."
    
    def unknown_intent(self, user_text: str) -> str:
        return "I'm not sure how to help with that. Could you please rephrase?"
    