from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

@dataclass
class Timer:
    id: str
    duration_seconds: int
    created_at: datetime
    ends_at: datetime
    active: bool

    @staticmethod
    def create(duration_seconds: int, name: str = str(uuid4())) -> 'Timer': #Cria o timer colocando um id aleatório no mesmo caso não seja expecificado pelo user ou system

        now = datetime.utcnow()
        ends_at = now.timestamp() + duration_seconds

        return Timer(
            id=name,
            duration_seconds=duration_seconds,
            created_at=now,
            ends_at=ends_at,
            active=True
        )
    

    

