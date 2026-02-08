from lumi.domain.enums.recipe_intent_type import RecipeIntentType
from lumi.application.intent.intent_recipe_router_service import IntentRecipeRouterService
from lumi.application.recipe.recipe_service import RecipeService

class RecipeFlowService:
    def __init__(self):
        self.intent_router = IntentRecipeRouterService()
        self.recipe_service = RecipeService()

    def manage_recipe(self, session, user_text) -> str:

        intent = self.intent_router.detect(user_text)

        if not session.current_recipe or not session.current_recipe.active:
            return self.handle_no_active_recipe(session, user_text, intent)
        return self.handle_active_recipe(session, user_text, intent)
        
    
    def handle_no_active_recipe(self, session, user_text, intent):
        print("Status: no recipe active path")
        print(f"Status: Intent - {intent}")
        match intent:
            case RecipeIntentType.RECIPE_REQUEST:
                return self.recipe_request(session,user_text)
            case RecipeIntentType.RECIPE_SUGESTION:
                return self.recipe_suggestion(user_text)
            case _:
                return "Não entendi o comando!"
        
    
    def handle_active_recipe(self, session, user_text, intent):
        print("Status: recipe active path")
        print(f"Status: Intent - {intent}")
        match intent:
       
            case RecipeIntentType.NEXT_STEP:
                return self.next_step(session)
            
            case RecipeIntentType.PREVIOUS_STEP:
                return self.previous_step(session)
            
            case RecipeIntentType.ACTUAL_STEP:
                return self.actual_step(session)
            
            case RecipeIntentType.LIST_RECIPE:
                return self.list_ingredients(session)
            
            case RecipeIntentType.IMAGE_ANALYSIS:
                return self.image_analysis(user_text)

            case _:
                return "Não entendi o comando da receita!"

    def list_ingredients(self, session):
        ingredients = session.current_recipe.list_ingredients()
        print(ingredients)
            
        return ingredients

    def actual_step(self,session) -> str:
        actual_step = session.current_recipe.get_current_step()
        print(actual_step)
        return actual_step

    def previous_step(self, session) -> str:
        previous_step = session.current_recipe.previus_step()
        if not previous_step:
            print("Não Possui Passo anterior")
            return "Não Possui Passo anterior"
        
        print(previous_step)
        return previous_step

    def next_step(self, session) -> str:
        next_step = session.current_recipe.next_step()
        print(next_step)
        if not next_step:
            session.current_recipe = None
            return "Receita Finalizada"
        return next_step

    def recipe_request(self, session, user_text: str) -> str:
        
        recipe_session = self.recipe_service.create_recipe_session(user_text)
        
        if not recipe_session:
            return "Receita não encontrada"
        
        session.current_recipe = recipe_session
        recipe_description = session.current_recipe.get_recipe_description()
        return recipe_description + "Lets Start?"

    def image_analysis(self, user_text: str) -> str:
        return "Please upload an image for analysis."

    def recipe_suggestion(self, user_text: str) -> str:
            recipes = self.recipe_service.list_recipes()
            recipe_names = ', '.join([recipe.name for recipe in recipes])
            return f"Here are some recipe suggestions: {recipe_names}."