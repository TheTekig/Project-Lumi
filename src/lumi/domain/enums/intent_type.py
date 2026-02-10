from enum import Enum

class IntentType(Enum): #Intenções 
    GREETING = "greeting"

    TIMER_CREATE = "timer_create"
    MANAGE_RECIPE = "manage_recipe"

    FREE_CHAT = "free_chat"
    
