from lumi.application.services.timer_service import TimerService

class ProcessIAInputCase:
    def __init__(self):
        self.timer = TimerService()

    def ia_process(self,ia_response):
        
        if "[CREATE_TIME]" in ia_response :
            clean_text = ia_response.replace("[CREATE_TIMER]", "")
            
            duration = self.timer.parse_time(clean_text)
            alarm_id = self.time.parse_timer_name(clean_text)
            self.timer.create_timer(alarm_id, duration, lambda timer:print("Timer: {timer.id} - Ended"))
            
            return clean_text
            pass
        
        elif "[CREATE_RECIPE]" in ia_response:
            clean_text = ia_response.replace("[CREATE_TIMER]", "")
            return clean_text

        elif "[NEXT_STEP]" in ia_response:
            clean_text = ia_response.replace("[CREATE_TIMER]", "")
            return clean_text

        elif "[START_RECIPE]" in ia_response:
            clean_text = ia_response.replace("[CREATE_TIMER]", "")
            return clean_text

        else:
            return ia_response
        

