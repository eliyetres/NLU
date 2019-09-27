from tdm.lib.device import DddDevice, DeviceWHQuery
from urllib2 import Request,urlopen 
import json



def getData(self,city,country):
    key = "378ff1bfe6cbfe897ddddf2bf5dbd60d"
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s' % (city,country,key)
    print(url)
    request = Request(url)
    response = urlopen(request)
    data = response.read()
    return json.loads(data)

class WeatherDevice(DddDevice):

    LONDON = "city_london"
    GOTHENBURG = "city_gothenburg"

    CITIES = {
        "London":LONDON,
        "Gothenburg": GOTHENBURG
    }

    ENGLAND = "country_uk"
    SWEDEN = "country_swe"

    TEMPERATURE = "temperature"
    WEATHER = "weather"

    class temperature(DeviceWHQuery):
        def perform(self,city,country):
           data = self.device.getData(city, country)
           temp = data['main']['temp']
           tempstr = str(temp)
           return [tempstr]

    class weather(DeviceWHQuery):
        def perform(self,city,country):
           data = self.device.getData(city, country)
           we = data['weather']['description']
           westr = str(we)
           return [westr]


# class WeatherDevice(DddDevice):
#     class WeatherRecognizer(EntityRecognizer):
#         """Entity recognizer for Weather"""

#         def recognize(self, utterance, language):
#             """Recognize entities in a user utterance, given the specified language.

#             This method is responsible for finding all dynamic entities in the utterance. Its accuracy affects the
#             behaviour of the dialogue system.

#             Since the search is conducted during runtime, particular care should be taken to ensure that the method is
#             accurate, robust and has sufficient performance.

#             Args:
#                 utterance (str): The utterance to be searched. For example 'call John'.
#                 language  (str): The language code of the utterance according to the ISO 639-2/B standard.
#                                  Exceptions are Swedish ('sv' instead of 'swe') and Italian ('it' instead of 'ita').

#             Returns:
#                 list of dicts: Given the example utterance "call John", the following entity could be returned
#                 [
#                     {
#                         "sort": "contact",       # The sort must be declared in the ontology.
#                         "grammar_entry": "John", # The grammar entry as it occurred in 'utterance'.
#                         "name": "contact_john",  # [optional] Should be a globally unique identifier. Must never be
#                                                  # found as is in a user utterance. Use for example the form Sort_ID
#                                                  # (e.g. contact_john).
#                     },
#                 ]
#             """
#             return []
