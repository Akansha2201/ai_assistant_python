import requests

url = "https://official-joke-api.appspot.com/random_joke"

json_data = requests.get(url).json()

tellMeJoke=["",""] 

tellMeJoke[0]=json_data["setup"]
tellMeJoke[1]=json_data["punchline"]

def joke():
    return tellMeJoke