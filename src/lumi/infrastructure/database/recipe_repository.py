from lumi.domain.entities.recipe import Recipe
import json

class RecipeRepository:
    def __init__(self):
        self._recipes = {}
        self.load_recipes_from_json('./lumi/infrastructure/database/recipes.json')

    def load_recipes_from_json(self, file_path: str):
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)

            for key, item in data.items():
                recipe = Recipe(
                    name=item['name'],
                    ingredients=item['ingredients'],
                    description=item['description'],
                    steps=item['steps']
                )
                self._recipes[key.lower()] = recipe

    def get_recipe_by_name(self, name: str) -> Recipe | None:
        print(name)
        recipe = self._recipes.get(name.lower())
        if not recipe:
            print("receita não encontrada")
        return recipe
    
    def list_all_recipes(self) -> list[Recipe]:
        return list(self._recipes.values())