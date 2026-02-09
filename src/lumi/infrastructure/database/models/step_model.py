from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lumi.infrastructure.database.session import Base

class StepModel(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    step_number = Column(Integer)
    text = Column(String)

    recipe = relationship("RecipeModel", back_populates="steps")
