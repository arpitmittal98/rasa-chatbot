from datetime import datetime
import datetime as dt

class CheckCurrentTime(Action): 
    def name(self): # type: () -> Text 
        return "action_check_time"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

        now = dt.datetime.now()
        today18pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
        today13am = now.replace(hour=13, minute=0, second=0, microsecond=0)
        message = 'Sure I have scheduled a cleaning for' + now
    
        dispatcher.utter_message(message)
        return []