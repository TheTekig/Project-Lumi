from dataclasses import dataclass, field
from datetime import datetime
from lumi.domain.entities.recipe_session import RecipeSession

@dataclass
class ConversationSession:
    id: str
    last_message: str | None = None
    last_intent: str | None = None
    current_recipe: RecipeSession | None = None
    current_step: int = 0
    created_at: datetime = field(default_factory=datetime.utcnow)