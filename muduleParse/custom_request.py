import requests as requests


class CustomRequest:
    def __init__(self):
        self.url_weather = 'http://api.openweathermap.org/data/2.5/find'
        self.units = 'metric'
        self.lang = 'ru'

    def send_request(self, url, city_id, app_id) -> dict:
        try:
            res = requests.get(url, params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
            return res.json()
        except Exception as e:
            print("Exception (weather):", e)
            pass
