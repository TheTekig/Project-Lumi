from sqlalchemy.orm import Session
from infrastructure.database.models.recipe_model import RecipeModel
from lumi.domain.entities.recipe import Recipe

class RecipeRepository:
    def __init__(self, db):
        self.db = db

    def get_by_name(self, name):
        model = self.db.query(RecipeModel).filter(
            RecipeModel.name.ilike(f"%{name}%")
        ).first()

        if not model:
            return None
        
        steps = [s.text for s in sorted(model.steps, key=lambda x: x.step_number)]
        ingredients = [f"{i.name} ({i.quantity})" for i in model.ingredients]

        return Recipe(
            name=model.name,
            description=model.description,
            steps=steps,
            ingredients=ingredients
        )