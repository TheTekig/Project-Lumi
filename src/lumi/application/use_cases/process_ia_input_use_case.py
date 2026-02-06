from lumi.application.timer.timer_service import TimerService
from lumi.application.dto.user_input_dto import UserInputDTO

import re

class ProcessIAInputCase:
    def __init__(self, user_input_use_case):
        self.timer = TimerService()
        self.user_input_uc = user_input_use_case


    def execute(self, ai_text: str, session_id:str ) -> str:
        clean_text, tags = self.extract_tags(ai_text)
        self.handle_tags(tags, session_id, clean_text)

        return clean_text

    def extract_tags(self, text):
        tags = re.findall(r'\[(.*?)\]', text)
        clean_text = re.sub(r'\[.*?\]', '', text).strip()
        return clean_text, tags
    
    def handle_tags(self, tags, session_id, clean_text):
        for tag in tags:
            if tag in ["CREATE_TIMER", "NEXT_STEP", "PREVIOUS_STEP", "REPEAT_STEP", "LIST_INGREDIENTS"]:
                dto = UserInputDTO(
                    message = clean_text,
                    session_id=session_id,
                    source="system"
                )
                self.user_input_uc.execute(dto)
            
                

