from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserInputDTO:
    def __init__(self,
    message: str,
    session_id: str,
    timestamp: datetime = datetime.utcnow(),
    source: str = "user"):
        self.message = message
        self.session_id = session_id
        self.source = source
        self.timestamp = timestamp
        

