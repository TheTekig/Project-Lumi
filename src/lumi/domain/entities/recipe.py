from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    steps: list[str]
    description: str
    ingredients: list[str]

    