from enum import Enum

class RecipeIntentType(Enum): #Intenções voltadas a manipulação das receitas

    RECIPE_REQUEST = "recipe_request"
    NEXT_STEP = "next_step"
    PREVIOUS_STEP = "previous_step"
    ACTUAL_STEP = "actual_step"
    IMAGE_ANALYSIS = "image_analysis"   
    RECIPE_DETAILS = "recipe_details"
    LIST_RECIPE = "list_recipe"
    RECIPE_SUGESTION = "recipe_suggestion"