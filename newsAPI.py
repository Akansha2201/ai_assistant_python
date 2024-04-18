import requests
from ss import *

api_address = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + news_API_key #update with your API key

json_data = requests.get(api_address).json()

newsHeadLines=[]

def news():
    for i in range(10):
        newsHeadLines.append("Number " + str(i + 1) + " , " + json_data["articles"][i]["title"]+".")
        
    return newsHeadLines

# newsHeadLines=news()
# print(newsHeadLines)