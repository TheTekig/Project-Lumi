from lumi.infrastructure.database.recipe_repository import RecipeRepository
from lumi.domain.entities.recipe_session import RecipeSession

import re

class RecipeService:
    def __init__(self):
        self.recipe_repository = RecipeRepository()
        self.recipe_session: RecipeSession

    def parse_recipe_name(self, user_text) -> str | None: #Resposavel por extrair o nome da receita no input do user
        message = user_text.lower() #Define o input string do usuario como minusculo para facilitar a extração
        
        pattern = r"""
(?:como\s+(?:eu\s+)?)?
(?:quero\s+|me\s+ensina\s+a\s+|ensina\s+a\s+|me\s+mostra\s+como\s+|vamos\s+)?
(?:fazer|preparar|cozinhar|montar|criar)?\s*
(?:a\s+)?
(?:receita\s+(?:de\s+)?)?
(?P<recipe>[a-zA-Zà-úÀ-Ú\s]+?)
(?:\s+(?:por\s+favor|pra\s+mim|para\s+mim|agora|hoje|aqui))?$
"""

        match = re.search(pattern, message, re.VERBOSE)

        if not match:
            return None
        
        recipe = match.group("recipe")

        recipe = re.sub(r'\b(por favor|pra mim|para mim|agora|hoje|aqui)\b', '', recipe).strip()
        
        return recipe if recipe else None


    def create_recipe_session(self, user_text) -> RecipeSession: #Cria a sessão da receita

        name = self.parse_recipe_name(user_text)
        recipe = self.recipe_repository.get_recipe_by_name(name) #Busca a receita no repositório pelo nome
        session = RecipeSession(recipe)
        return session

        
        
    def list_recipes(self): #Lista todas as receitas do repositorio
        return self.recipe_repository.list_all_recipes()

