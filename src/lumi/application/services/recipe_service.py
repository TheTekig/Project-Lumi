from lumi.infrastructure.database.recipe_repository import RecipeRepository
from lumi.domain.entities.recipe_session import RecipeSession

import re

class RecipeService:
    def __init__(self):
        self.recipe_repository = RecipeRepository()
        self.recipe_session = RecipeSession()

    def parse_recipe_name(self, user_text) -> str | None:
        message = user_text.lower()
        
        pattern = r"""
        (?:como\s+)?
        (?:fazer|preparar|cozinhar|montar|criar|ensinar|aprender|quero|vamos)?\s*
        (?:a\s+)?
        (?:receita\s+(?:de\s+)?)?
        (?P<recipe>.+)
"""
        match = re.search(pattern, message, re.VERBOSE)

        if not match:
            return None
        
        recipe = match.group("recipe")

        recipe = re.sub(r'\b(por favor|pra mim|para mim|agora|hoje|aqui)\b', '', recipe).strip()
        
        return recipe if recipe else None

    def create_recipe_session(self, user_text):

        name = self.parse_recipe_name(user_text)
        recipe = self.recipe_repository.get_recipe_by_name(name)
        session = RecipeSession(recipe)
        return session

        
        
    def list_recipes(self):
        return self.recipe_repository.list_all_recipes()

