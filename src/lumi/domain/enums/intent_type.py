from enum import Enum

class IntentType(Enum):
    GREETING = "greeting"
    TIMER_CREATE = "timer_create"
    RECIPE_REQUEST = "recipe_request"
    FREE_CHAT = "free_chat"
    CONFIRMATION = "confirmation"
