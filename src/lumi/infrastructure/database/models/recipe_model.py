from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import relationship
from lumi.infrastructure.database.session import Base

class RecipeModel(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)

    steps = relationship("StepModel", back_populates="recipe")
    ingredients = relationship("IngredientModel", back_populates="recipe")