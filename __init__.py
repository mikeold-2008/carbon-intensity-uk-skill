from datetime import date
from mycroft import MycroftSkill, intent_file_handler
import requests 


class CarbonIntensityUk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('uk.intensity.carbon.intent')
    def handle_uk_intensity_carbon(self, message):
        intensity = 'house'
        
        self.speak_dialog('uk.intensity.carbon', data={
            'intensity': intensity
        })

        
        def stop(self):
        pass
        

def create_skill():
    return CarbonIntensityUk()

