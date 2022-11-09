
from mycroft import MycroftSkill, intent_file_handler
from datetime import date
import requests 


class CarbonIntensityUk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('uk.intensity.carbon.intent')
    def handle_uk_intensity_carbon(self, message):
        intensity = requests.get("https://api.carbonintensity.org.uk/intensity").json()['data'][0]
        #intensity = "house tall"

        self.speak_dialog('uk.intensity.carbon', data={
            'intensity': intensity
        })


        

def create_skill():
    return CarbonIntensityUk()

