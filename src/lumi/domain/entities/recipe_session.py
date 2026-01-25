from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import uuid4

@dataclass
class RecipeSession:
    id: str
    recipe_name: str
    started_at: datetime
    last_interaction_at: datetime
    is_active: bool
    steps : list[str]
    current_step_index: int
    
