from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    api_key = open("API_KEY","r").read()
    print(api_key)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    city = 'Kerala'
    city_weather = requests.get(url.format(city,api_key)).json()
    print(city_weather)
    return render(request, 'weather_app/index.html')