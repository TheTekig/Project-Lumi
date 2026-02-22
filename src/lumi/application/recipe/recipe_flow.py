from lumi.domain.enums.recipe_intent_type import RecipeIntentType
from lumi.application.intent.intent_recipe_router_service import IntentRecipeRouterService
from lumi.application.recipe.recipe_service import RecipeService
from lumi.infrastructure.event_bus.event_bus import event_bus

class RecipeFlowService: #Classe responsavel pelo controle de ações envolvendo receitas
    def __init__(self):
        self.intent_router = IntentRecipeRouterService()
        self.recipe_service = RecipeService()

    def manage_recipe(self, session, user_text, input_source) -> str: #Método identifica a inteção para receita e redireciona para métodos utilizaveis com receitas ativas e receitas inativas

        intent = self.intent_router.detect(user_text) # Identifica Inteção com base no input do usuario

        if not session.current_recipe or not session.current_recipe.active: #Verifica se a sessão que estamos não possui uma receita ou se não possui uma receita ativa
            response = self.handle_no_active_recipe(session, user_text, intent) #Chama Método para receitas inativas

        else:
            response = self.handle_active_recipe(session, user_text, intent) #Chama Método para receitas ativas

        if input_source == "system": #Verifica se o input teve origem do systema (comumente disparado pela IA)
            event_bus.publish({"type": "AI-System Request", "message": f"{response}" }) #Envia a resposta para a lista de eventos onde sera enviado ao output(lumi-robot)
            """Sem a utilização do event_bus nesse local a receita não seria dita pela lumi, 
            pois a requisição HTTP ja foi concluida com a resposta da IA, então é necessario o envio do desdobrar apartir da lista de eventos"""
        return response
        
    
    def handle_no_active_recipe(self, session, user_text, intent): #Método responsavel pelos métodos de receita inativa
        print("Status: no recipe active path")
        print(f"Status: Intent - {intent}")
        match intent:
            case RecipeIntentType.RECIPE_REQUEST:
                return self.recipe_request(session,user_text) #Faz a requisição da receita que o usuário quer
            case RecipeIntentType.RECIPE_SUGESTION:
                return self.recipe_suggestion(user_text) #Faz uma sugestão de receita com base noque o usuário pediu com oque temos no banco de dados (Feature em desenvolvimento)
            case _:
                return "Não entendi o comando!"
        
    
    def handle_active_recipe(self, session, user_text, intent): #Método responsavel pelos métodos de receita inativa
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

    def list_ingredients(self, session): # Lista os ingredientes
        ingredients = session.current_recipe.list_ingredients()
        print(ingredients)
            
        return ingredients

    def actual_step(self,session) -> str: # Repete o passo atual da receita
        actual_step = session.current_recipe.get_current_step()
        print(actual_step)
        return actual_step

    def previous_step(self, session) -> str: # Retorna a um passo anterior da receita
        previous_step = session.current_recipe.previus_step()
        if not previous_step:
            print("Não Possui Passo anterior")
            return "Não Possui Passo anterior"
        
        print(previous_step)
        return previous_step

    def next_step(self, session) -> str: # Avança para o próximo passo da receita
        next_step = session.current_recipe.next_step()
        print(next_step)
        if not next_step:
            session.current_recipe = None
            return "Receita Finalizada"
        return next_step

    def recipe_request(self, session, user_text: str) -> str: # Faz a requisição da receita 
        
        recipe_session = self.recipe_service.create_recipe_session(user_text) #Cria uma sessão de receita que sera vinculado ao session
        
        if not recipe_session: 
            return "Receita não encontrada"
        
        session.current_recipe = recipe_session #Vincula a receita atual a sessão atual
        recipe_description = session.current_recipe.get_recipe_description() #Faz uma descrição breve da receita escolhida
        return recipe_description + ", Vamos Começar?"

    def image_analysis(self, user_text: str) -> str: #Analisa a imagem do processo atual da receita (Feature em desenvolvimento)
        return "Please upload an image for analysis."

    def recipe_suggestion(self, user_text: str) -> str: #Atualmente Lista todas as receitas que possui
            recipes = self.recipe_service.list_recipes()
            recipe_names = ', '.join([recipe.name for recipe in recipes])
            return f"Here are some recipe suggestions: {recipe_names}."