from lumi.application.timer.timer_service import TimerService
from lumi.application.dto.user_input_dto import UserInputDTO

import re

class ProcessIAInputCase: # Classe Responsavel pelo tratamento de mensagem feitas pela IA
    def __init__(self, user_input_use_case):
        self.timer = TimerService()
        self.user_input_uc = user_input_use_case


    def execute(self, ai_text: str, session_id:str ) -> str: # Executa oque a IA passou para o sistema
        clean_text, tags = self.extract_tags(ai_text) # Faz separação e extração das Tags colocadas ao final do retorno da resposta da IA e a extração do texto como todo
        self.handle_tags(tags, session_id, clean_text) # Faz a ação determinada pela Tag colocada

        return clean_text #Retorna oque a IA respondeu a fala do usuario

    def extract_tags(self, text): #Extração de tag e clean_text
        tags = re.findall(r'\[(.*?)\]', text)
        clean_text = re.sub(r'\[.*?\]', '', text).strip()
        return clean_text, tags
    
    def handle_tags(self, tags, session_id, clean_text):
        for tag in tags:
            if tag in ["CREATE_TIMER", "NEXT_STEP", "PREVIOUS_STEP", "REPEAT_STEP", "LIST_INGREDIENTS"]: #Verifica se a tag encontrada pertence a alguma das seguintes
                dto = UserInputDTO(
                    message = clean_text,
                    session_id=session_id,
                    source="system"
                ) #Realiza um input como "systema" para o processamento pelo user_input, reaproveitando o processamento presente no process_user_input_use_case.
                self.user_input_uc.execute(dto)
            
                

