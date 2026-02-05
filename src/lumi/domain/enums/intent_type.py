from enum import Enum

class IntentType(Enum):
    GREETING = "greeting"

    TIMER_CREATE = "timer_create"

    RECIPE_REQUEST = "recipe_request"
    MANAGE_RECIPE = "manage_recipe"
    NEXT_STEP = "next_step"
    PREVIOUS_STEP = "previous_step"
    ACTUAL_STEP = "actual_step"
    IMAGE_ANALYSIS = "image_analysis"   
    RECIPE_DETAILS = "recipe_details"

    FREE_CHAT = "free_chat"
    RECIPE_SUGESTION = "recipe_suggestion"
    
