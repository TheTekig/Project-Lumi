from lumi.domain.entities.recipe import Recipe

class RecipeRepository:
    def __init__(self):
        self._recipes : {
            "Pancakes": Recipe(
                name="Pancakes",
                ingredients=["1 cup flour", "2 tablespoons sugar", "1 tablespoon baking powder", "1 cup milk", "1 egg", "2 tablespoons melted butter"],
                steps=[
                    "In a bowl, mix flour, sugar, and baking powder.",
                    "In another bowl, whisk milk, egg, and melted butter.",
                    "Combine wet and dry ingredients until just mixed.",
                    "Heat a non-stick pan over medium heat.",
                    "Pour 1/4 cup batter for each pancake.",
                    "Cook until bubbles form, then flip and cook until golden."
                ]
            ),

            "White Rice": Recipe(
                name="White Rice",
                ingredients=["1 cup white rice", "2 cups water", "1/2 teaspoon salt", "1 tablespoon butter (optional)"],
                steps=[
                    "Rinse the rice under cold water until the water runs clear.",
                    "In a pot, bring water to a boil.",
                    "Add salt and butter to the boiling water.",
                    "Stir in the rice, reduce heat to low, and cover the pot.",
                    "Simmer for 18-20 minutes, or until the water is absorbed and rice is tender.",
                    "Remove from heat and let it sit, covered, for 5 minutes. Fluff with a fork before serving."
                ]
            )
        } 
    def get_recipe_by_name(self, name: str) -> Recipe | None:
        return self._recipes.get(name.lower())
    
    def list_all_recipes(self) -> list[Recipe]:
        return list(self._recipes.values())