from enum import Enum

class IntentType(Enum):
    GREETING = "greeting"
    TIMER_CREATE = "timer_create"
    RECIPE_REQUEST = "recipe_request"
    FREE_CHAT = "free_chat"
    CONFIRMATION = "confirmation"
    SMALL_TALK = "small_talk"
    IMAGE_ANALYSIS = "image_analysis"
    RECIPE_SUGESTION = "recipe_suggestion"
