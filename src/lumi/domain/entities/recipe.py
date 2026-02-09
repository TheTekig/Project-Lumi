from dataclasses import dataclass

@dataclass
class Recipe:
    def __init__(self, name, description, steps, ingredients):

        self.name = name
        self.steps = steps
        self.description = description
        self.ingredients = ingredients

    