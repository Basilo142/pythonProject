import pprint
import requests

class Weather:

    def get(self, city):

        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=c1880474f9e70d14e25f9e35c8319424&units=metric"
        data = requests.get(url).json()

class CityInfo:
    def __init__(self, city):
        self.city = city

    def weather_forecast(self):
        pass




def _main():
    city_info = CityInfo('Kyiv')
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)


if __name__ =="__main__":
    _main()