from urllib import response
import requests

API_KEY = "2be556f4759ac4ac92bcf97767cbdd1f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][0]['main'] + "; " + data['weather'][0]['description']
    temp = str(round(data['main']['temp'] - 273.15, 2)) + "°C"
    coords = str(data['coord']['lon']) + " | " + str(data['coord']['lat'])

else:
    print("lol idiot some shiz happened")
