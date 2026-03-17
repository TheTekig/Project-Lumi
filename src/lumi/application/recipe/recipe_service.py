from lumi.infrastructure.database.recipe_repository import RecipeRepository
from lumi.domain.entities.recipe_session import RecipeSession

import re

class RecipeService:
    def __init__(self):
        self.recipe_repository = RecipeRepository()
        self.recipe_session: RecipeSession

    def parse_recipe_name(self, user_text) -> str | None: #Resposavel por extrair o nome da receita no input do user
        if not user_text:
            return None

        text = user_text.lower().strip()

        # remover wake words comuns
        text = re.sub(r'\b(lumi|assistente|bot)\b', '', text).strip()

        pattern = r"""
        (?:
            como\s+(?:eu\s+)?(?:fazer|faz|preparar|cozinhar) |
            (?:me\s+ensina\s+a\s+|me\s+mostra\s+como\s+) |
            (?:quero\s+|vamos\s+|preciso\s+)?(?:fazer|preparar|cozinhar) |
            receita\s+(?:de\s+)?
        )
        \s*
        (?:um\s+|uma\s+|o\s+|a\s+|de\s+)?
        (?P<recipe>[a-zà-ú\s]+)
        """

        match = re.search(pattern, text, re.VERBOSE)

        if not match:
            return None

        recipe = match.group("recipe")

        # remover lixo no final
        recipe = re.sub(
            r'\b(por favor|pra mim|para mim|agora|hoje|aqui|passo a passo)\b',
            '',
            recipe
        )

        # remover artigos iniciais
        recipe = re.sub(r'^(um|uma|o|a|de)\s+', '', recipe)

        recipe = recipe.strip()

        if not recipe:
            return None

        return recipe


    def create_recipe_session(self, user_text) -> RecipeSession: #Cria a sessão da receita

        name = self.parse_recipe_name(user_text)
        recipe = self.recipe_repository.get_recipe_by_name(name) #Busca a receita no repositório pelo nome
        session = RecipeSession(recipe)
        return session

        
        
    def list_recipes(self): #Lista todas as receitas do repositorio
        return self.recipe_repository.list_all_recipes()

