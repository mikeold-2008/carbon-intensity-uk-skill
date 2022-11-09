import requests 
BASE_URL = "https://api.carbonintensity.org.uk/intensity"
from mycroft import MycroftSkill, intent_file_handler


class CarbonIntensityUk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('uk.intensity.carbon.intent')
    def handle_uk_intensity_carbon(self, message):
        intensity = ''
        intensity = requests.get(BASE_URL).json()['data'][0]

        self.speak_dialog('uk.intensity.carbon', data={
            'intensity': intensity
        })


def create_skill():
    return CarbonIntensityUk()

