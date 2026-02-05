import re
from lumi.domain.enums.intent_type import IntentType
class IntentRouterService:

    def detect(self, message: str) -> IntentType:
        message = message.lower()

        if  any(word in message for word in ["hello", "hey", "oi", "ola", "saudações"]):
            return IntentType.GREETING
        
        if re.search(r'(?:\b(set|create|start|começar|colocar|coloca|adicionar|iniciar|inicia)\b\s*)?(?:um|o\s+)?\b(timer|alarme|alarm|lembrete|cron[oô]metro)\b', message):
            return IntentType.TIMER_CREATE  

        if any(word in message for word in ["recipe", "how to make", "cook", "receita", "preparar", "como fazer"]):
            return IntentType.RECIPE_REQUEST
        
        if any(word in message for word in [
            "next step", "next", "próximo passo", "próximo", "seguinte",
            "previous step", "previous", "passo anterior", "anterior",
            "actual step", "execute step", "execute", "atual passo", "atual",
            "repeat step", "repeat", "repita passo", "repita",
            "list ingredients", "ingredients", "lista de ingredientes", "ingredientes",
            "whatsapp", "analyze image", "analisar imagem",
            ]):
            return IntentType.MANAGE_RECIPE

        return IntentType.FREE_CHAT