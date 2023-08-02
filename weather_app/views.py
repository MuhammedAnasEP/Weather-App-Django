from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    api_key = open("API_KEY","r").read()
    print(api_key)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    city = 'malappuram'
    city_weather = requests.get(url.format(city,api_key)).json()

    weather = {
        'city': city,
        'temprature': round((city_weather['main']['temp']-32)*(5/9),2),
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {
        'weather': weather
    }

    print(city_weather)
    return render(request, 'weather_app/index.html',context)