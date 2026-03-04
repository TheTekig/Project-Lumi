import re
from lumi.domain.enums.recipe_intent_type import RecipeIntentType

class IntentRecipeRouterService: #Classe responsavel por detectar a intenção do usuário através de palavras chaves para manipulação de receitas

    def detect(self, message) -> RecipeIntentType: # detect somente retorna a intenção do usuario
       
        #if any(word in message for word in [
           # "recipe", "how to make", "cook", "receita", "preparar", "como fazer", 
           # "quero fazer", "quero preparar", "quero cozinhar", "me ensina a fazer", "me ensina a preparar",
          #  "me ensina a cozinhar", "ensina a fazer", "ensina a preparar", "ensina a cozinhar",
          #  "como eu faço", "como eu preparo", "como eu cozinho", "me mostra como fazer", "me mostra como preparar", "me mostra como cozinhar"
          #  ]):
          
        intent_pattern = r"""
                    \b(
                    como\s+(?:eu\s+)?(fazer|preparar|cozinhar)|
                    quero\s+(fazer|preparar|cozinhar)|
                    receita\s+de|
                    how\s+to\s+make|
                    cook
                    )\b
                    """
        if re.search(intent_pattern, message, re.IGNORECASE | re.VERBOSE):
            return RecipeIntentType.RECIPE_REQUEST

        if any(word in message for word in ["whatsapp", "analyze image", "analisar imagem"]):
            return RecipeIntentType.IMAGE_ANALYSIS

        if any(word in message for word in [
            "list ingredients", "ingredients", "lista de ingredientes", "ingredientes", "listar os ingredientes",
            "quais os ingredientes", "quais os ingredientes necessários", "quais os ingredientes para essa receita", "quais os ingredientes para essa etapa",
            "lista os ingredientes"
            ]):
            return RecipeIntentType.LIST_RECIPE

        if any(word in message for word in [
            "repeat step", "repeat", "repita passo", "repita",
            "actual step", "execute step", "execute", "atual passo", "atual",
            "repete o passo", "repete a etapa", "fala denovo", "oque tenho que fazer", "oque tenho que fazer agora",
            "oque tenho que fazer mesmo", "pode repetir" 
            ]):
            return RecipeIntentType.ACTUAL_STEP
        
        if any(word in message for word in [
            "previous step", "previous", "passo anterior", "anterior", "voltar passo", "voltar", "retornar passo", "retornar",
            "passo anterior", "anterior", "voltar passo", "voltar", "retornar passo", "retornar",
            "antes", "voltar para o passo anterior", "voltar para a etapa anterior", "voltar para o passo anterior", "voltar para a etapa anterior","ja terminei", "ja fiz", "ja fiz esse passo", "ja fiz essa etapa", "ja terminei esse passo", "ja terminei essa etapa", 
            "voltar para o passo anterior", "voltar para a etapa anterior", "retornar para o passo anterior", "retornar para a etapa anterior", "retornar para o passo anterior", "retornar para a etapa anterior"
                                            ]):
            return RecipeIntentType.PREVIOUS_STEP

        if any(word in message for word in [
            "next step", "next", "próximo passo", "próximo", "seguinte", "avançar", "avancar", "terminei", "terminei passo", "terminei etapa", "terminei essa etapa",
            "terminei o passo", "terminei a etapa", "terminei essa passo", "terminei essa etapa", "próximo passo", "próximo", "seguinte", "avançar", "avancar",
            "continuar", "continuar para o próximo passo", "continuar para a próxima etapa", "continuar para o próximo", "continuar para a seguinte etapa", "continuar para a seguinte",
            "continuar para o próximo passo", "continuar para o próximo", "continuar para a seguinte etapa", "continuar para a seguinte", "próximo passo", "próximo", "seguinte", "avançar", "avancar"
            ]):
            return RecipeIntentType.NEXT_STEP