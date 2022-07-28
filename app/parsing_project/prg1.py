
# this secret key! It must be in env variables. It's only tests fot instat
from module_parse.custom_request import CustomRequest

API_KEY = '97de9c699d9b29dcd47fa95436c89380'


def get_weathermap():
    c_r = CustomRequest()
    data = c_r.send_request(
        url='http://api.openweathermap.org/data/2.5/weather',
        city_id='2643743',
        app_id=API_KEY
    )
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])


if __name__ == '__main__':
    get_weathermap()
