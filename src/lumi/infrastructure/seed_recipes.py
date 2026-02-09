from lumi.infrastructure.database.session import SessionLocal
from lumi.infrastructure.database.models.recipe_model import RecipeModel
from lumi.infrastructure.database.models.step_model import StepModel
from lumi.infrastructure.database.models.ingredient_model import IngredientModel

db = SessionLocal()

frango = RecipeModel(
    name= "Frango grelhado",
    description="Um frango simples e saboroso para o dia a dia"
)

db.add(frango)
db.commit()
db.refresh(frango)

Ingredients = [
    IngredientModel(recipe_id=frango.id, name="Frango", quantity="500g"),
    IngredientModel(recipe_id=frango.id, name="Sal", quantity="a gosto"),
    IngredientModel(recipe_id=frango.id, name="Alho", quantity="2 dentes")
]

steps =[
    StepModel(recipe_id=frango.id, step_number=1, text="Tempere o frango"),
    StepModel(recipe_id=frango.id, step_number=2, text="Aqueça a frigideira"),
    StepModel(recipe_id=frango.id, step_number=3, text="Grelhe até dourar")
]

db.add_all(Ingredients + steps)
db.commit()

print("Receita adicionada com sucesso!")