import requests



api_key = '30d4741c779ba94c470ca1f63045390a'

user_city = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&units=metric&APPID={api_key}")
print(f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&units=metric&APPID={api_key}")
print(weather_data.status_code)

weather_now = weather_data.json()['weather'][0]['main']
temperature = weather_data.json()['main']['temp']

print(f'The weather in {user_city} is: {weather_now}')
print(f'The temperature in {user_city} is: {temperature} Cº')