import re
from lumi.domain.enums.intent_type import IntentType

class IntentRouterService: #Classe responsavel por identificar inteção do usuário para direcionalo para saida desejada

    def detect(self, message: str) -> IntentType: #Retorna somente a intenção do usuário
        message = message.lower()

        if  any(word in message for word in ["hello", "hey", "ola", "saudações"]):
            return IntentType.GREETING
        
        if re.search(r'(?:\b(set|create|start|começar|colocar|coloca|adicionar|iniciar|inicia)\b\s*)?(?:um|o\s+)?\b(timer|alarme|alarm|lembrete|cron[oô]metro)\b', message):
            return IntentType.TIMER_CREATE  
        
        if any(word in message for word in [
            "recipe", "how to make", "cook", "receita", "preparar", "como fazer", 
            "quero fazer", "quero preparar", "quero cozinhar", "me ensina a fazer", "me ensina a preparar",
            "me ensina a cozinhar", "ensina a fazer", "ensina a preparar", "ensina a cozinhar",
            "como eu faço", "como eu preparo", "como eu cozinho", "me mostra como fazer", "me mostra como preparar", "me mostra como cozinhar",
            "list ingredients", "ingredients", "lista de ingredientes", "ingredientes", "listar os ingredientes",
            "quais os ingredientes", "quais os ingredientes necessários", "quais os ingredientes para essa receita", "quais os ingredientes para essa etapa",
            "lista os ingredientes","repeat step", "repeat", "repita passo", "repita",
            "actual step", "execute step", "execute", "atual passo", "atual",
            "repete o passo", "repete a etapa", "fala denovo", "oque tenho que fazer", "oque tenho que fazer agora",
            "oque tenho que fazer mesmo", "pode repetir","previous step", "previous", "passo anterior", "anterior", "voltar passo", "voltar", "retornar passo", "retornar",
            "passo anterior", "anterior", "voltar passo", "voltar", "retornar passo", "retornar",
            "antes", "voltar para o passo anterior", "voltar para a etapa anterior", "voltar para o passo anterior", "voltar para a etapa anterior","ja terminei", "ja fiz", "ja fiz esse passo", "ja fiz essa etapa", "ja terminei esse passo", "ja terminei essa etapa", 
            "voltar para o passo anterior", "voltar para a etapa anterior", "retornar para o passo anterior", "retornar para a etapa anterior", "retornar para o passo anterior", "retornar para a etapa anterior",
            "next step", "next", "próximo passo", "próximo", "seguinte", "avançar", "avancar", "terminei", "terminei passo", "terminei etapa", "terminei essa etapa",
            "terminei o passo", "terminei a etapa", "terminei essa passo", "terminei essa etapa", "próximo passo", "próximo", "seguinte", "avançar", "avancar",
            "continuar", "continuar para o próximo passo", "continuar para a próxima etapa", "continuar para o próximo", "continuar para a seguinte etapa", "continuar para a seguinte",
            "continuar para o próximo passo", "continuar para o próximo", "continuar para a seguinte etapa", "continuar para a seguinte", "próximo passo", "próximo", "seguinte", "avançar", "avancar"
            ]):
            return IntentType.MANAGE_RECIPE

        return IntentType.FREE_CHAT