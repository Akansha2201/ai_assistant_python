import requests
from ss import weather_API_key


api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Charlottesville&appid=' + weather_API_key #update with your API key

response = requests.get(api_address)
json_data = response.json()

def temp():
    temperature = round(json_data["main"]["temp"] - 273,1)
    return temperature

def descrip():
    description = json_data["weather"] [0] ["description"]
    return description
    
# print(temp())
# print(descrip())

# print(json_data)

