import re
from lumi.domain.enums.intent_type import IntentType
class IntentRouterService:

    def detect(self, message: str) -> IntentType:
        message = message.lower()

        if  any(word in message for word in ["hello", "hi", "hey"]):
            return IntentType.GREETING
        
        if re.search(r'\b(set|create|start)\b.*\b(timer|alarm|reminder)\b', message):
            return IntentType.TIMER_CREATE  

        if any(word in message for word in ["recipe", "how to make", "cook"]):
            return IntentType.RECIPE_REQUEST

        return IntentType.FREE_CHAT