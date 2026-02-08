from lumi.domain.entities.recipe import Recipe

class RecipeRepository:
    def __init__(self):
        self._recipes = {
            "recipe pancakes": Recipe(
                name="Pancakes",
                ingredients=["1 cup flour", "2 tablespoons sugar", "1 tablespoon baking powder", "1 cup milk", "1 egg", "2 tablespoons melted butter"],
                description= "A pancake is a flat, round, starch-based cake cooked on a hot griddle or frying pan, commonly made from flour, milk, eggs, and a leavening agent like baking powder.",
                steps=[
                    "In a bowl, mix flour, sugar, and baking powder.",
                    "In another bowl, whisk milk, egg, and melted butter.",
                    "Combine wet and dry ingredients until just mixed.",
                    "Heat a non-stick pan over medium heat.",
                    "Pour 1/4 cup batter for each pancake.",
                    "Cook until bubbles form, then flip and cook until golden."
                ]
            ),

            "recipe white rice": Recipe(
                name="White Rice",
                ingredients=["1 cup white rice", "2 cups water", "1/2 teaspoon salt", "1 tablespoon butter (optional)"],
                description= "White rice is a staple, refined, and highly versatile grain, specifically processed by removing the husk, bran, and germ to leave only the white starchy endosperm",
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
        print(name)
        recipe = self._recipes.get(name.lower())
        if not recipe:
            print("receita não encontrada")
        return recipe
    
    def list_all_recipes(self) -> list[Recipe]:
        return list(self._recipes.values())