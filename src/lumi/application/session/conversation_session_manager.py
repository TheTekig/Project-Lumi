from lumi.domain.entities.conversation_session import ConversationSession
from uuid import uuid4

class ConversationSessionManager: #Responsavel por criar as sessões de usuario

    def __init__(self):
        self.sessions : dict[str,ConversationSession] = {}

    def get_or_create(self, session_id: str | None):
        if session_id and session_id in self.sessions:
            return self.sessions[session_id]

        session = ConversationSession(id=session_id or str(uuid4()))
        self.sessions[session.id] = session
        return session