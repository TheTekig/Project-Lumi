from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    steps: list[str]
    ingredients: list[str]

    