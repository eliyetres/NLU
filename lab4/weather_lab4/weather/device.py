from tdm.lib.device import DddDevice, DeviceWHQuery
from urllib2 import Request,urlopen 
import json

class WeatherDevice(DddDevice):

    metric = "metric"
    imperial = "imperial"

    UNITS = {
        "celsius": metric, 
        "metric": metric, 
        "fahrenheit": imperial, 
        "imperial": imperial
    }

    def getUnit(self, unit):
        selected_unit = self.UNITS[unit]
        return selected_unit

    def getData(self, city, country, units="metric"):
        key = "378ff1bfe6cbfe897ddddf2bf5dbd60d"
        units = self.getUnit(units)
        url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&units=%s&APPID=%s' % (city,country,units,key)
        print(url)
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    class temperature(DeviceWHQuery):
        def perform(self, city, country, units="metric"):
            units = self.device.getUnit(units)
            data = self.device.getData(city, country, units)
            temp = data['main']['temp']
            tempstr = str(int(temp))
            print("Temp: ", tempstr, "units:", units)
            return [tempstr]

    class weather(DeviceWHQuery):
        def perform(self, city, country):
           data = self.device.getData(city, country)
           main_we = data['weather'][0]['main']
           we = data['weather'][0]['description']
           weather = str(main_we+" with "+we)
           if main_we.lower() == we:
               weather = main_we           
           print(weather)
           return [weather]
