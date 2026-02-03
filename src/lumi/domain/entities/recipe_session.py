from lumi.domain.entities.recipe import Recipe

class RecipeSession():
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
        return self.current_recipe.steps[self.current_step]

    def next_step(self):
        self.current_step += 1

        if self.current_step >= len(self.current_recipe.steps):
            self.active = False
            return None

        return self.get_current_step()        
    

