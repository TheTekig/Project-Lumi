from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserInputDTO:
    message: str
    session_id: str | None = None
    timestamp: datetime = datetime.utcnow()
