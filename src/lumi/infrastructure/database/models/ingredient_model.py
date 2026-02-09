from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import relationship
from lumi.infrastructure.database.session import Base

class IngredientModel(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    name = Column(String)
    quantity = Column(String)

    recipe = relationship("RecipeModel", back_populates="ingredients")
