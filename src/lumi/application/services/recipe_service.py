from lumi.infrastructure.database.recipe_repository import RecipeRepository
from lumi.domain.entities.recipe import Recipe

class RecipeService:
    def __init__(self):
        self.recipe_repository = RecipeRepository()

    def get_recipe(self, name: str) -> Recipe | None:
        recipe =  self.recipe_repository.get_recipe_by_name(name)

        if not recipe:
            return None
        
        return RecipeSession.create(
            recipe_name=recipe.name,
            ingredients=recipe.ingredients,
            steps=recipe.steps
        )

    def list_recipes(self) -> list[Recipe]:
        return self.recipe_repository.list_all_recipes()