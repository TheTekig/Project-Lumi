import re
from lumi.domain.enums.recipe_intent_type import RecipeIntentType

class IntentRecipeRouterService:

    def detect(self, message) -> RecipeIntentType:
       
        if any(word in message for word in ["recipe", "how to make", "cook", "receita", "preparar", "como fazer"]):
            return RecipeIntentType.RECIPE_REQUEST

        if any(word in message for word in ["whatsapp", "analyze image", "analisar imagem"]):
            return RecipeIntentType.IMAGE_ANALYSIS

        if any(word in message for word in ["list ingredients", "ingredients", "lista de ingredientes", "ingredientes"]):
            return RecipeIntentType.LIST_RECIPE

        if any(word in message for word in ["repeat step", "repeat", "repita passo", "repita",
            "actual step", "execute step", "execute", "atual passo", "atual"]):
            return RecipeIntentType.ACTUAL_STEP
        
        if any(word in message for word in ["previous step", "previous", "passo anterior", "anterior"]):
            return RecipeIntentType.PREVIOUS_STEP

        if any(word in message for word in ["next step", "next", "próximo passo", "próximo", "seguinte"]):
            return RecipeIntentType.NEXT_STEP