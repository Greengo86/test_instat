import asyncio

import aiohttp as aiohttp

from main import time_of_function

url = 'http://api.openweathermap.org/data/2.5/weather'
city_ids = ('2643743', '3143244', '3117735')
app_id = '97de9c699d9b29dcd47fa95436c89380'


async def write_in_file(data):
    try:
        with open('result.txt', "a") as f:
            id_ = data['id']
            temp = data['main']['temp']
            state_weather = data['weather'][0]['description']
            city = data['name']

            one_string = f'city - {city}, with id - {id_}, state_weather - {state_weather}, temp - {temp} grad'
            f.write(f'{one_string}\n')
    except Exception as err:
        print(f"Error in write accounts data in file - {err}")


async def request(client, city_id):
    resp = await client.get(url, params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
    result = await resp.json()
    await write_in_file(result)


@time_of_function
async def main():
    async with aiohttp.ClientSession() as client:
        task_list = []
        for id_ in city_ids:
            req = request(client, id_)
            task = asyncio.create_task(req)
            task_list.append(task)
        await asyncio.gather(*task_list)


if __name__ == '__main__':
    asyncio.run(main())
