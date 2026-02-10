from lumi.domain.entities.recipe import Recipe

class RecipeSession(): #Classe responsavel por armazenar a receita, o passo atual da receita, se a mesma esta ativa e os principais métodos para manipulação das mesmas
    def __init__(self, recipe):
        self.current_recipe : Recipe = recipe
        self.current_step: int = 0
        self.active: bool = True

    @classmethod
    def create(cls, recipe):
        session = cls()
        session.current_recipe = recipe
        session.current_step = 0
        session.active = True
        return session

    def get_current_step(self): 
        return self.current_recipe.steps[self.current_step - 1]
    
    def get_recipe_description(self) -> str:
        return self.current_recipe.description

    def next_step(self):
        self.current_step += 1

        if self.current_step >= len(self.current_recipe.steps):
            self.active = False
            return None

        return self.get_current_step()

    def previus_step(self):
        #if self.current_step < len(self.current_recipe.steps):
           # return "Não possui passo anterior"
        
        self.current_step -= 1

        return self.get_current_step()

    def list_ingredients(self):
        return "\n".join(f"➡ {i}" for i in self.current_recipe.ingredients)
    

