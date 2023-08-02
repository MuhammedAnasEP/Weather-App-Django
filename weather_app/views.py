from django.shortcuts import render
import requests
from .models import City

# Create your views here.

def index(request):
    api_key = open("API_KEY","r").read()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    if request.method == 'POST': 
        name = request.POST['name']
        try:
            city_weather = requests.get(url.format(name,api_key)).json()
            temprature = round((city_weather['main']['temp']-32)*(5/9),2)
            try:
                old = City.objects.get(name=name)
                old.delete()
            except:                
                new_name = City.objects.create(name=name)
                new_name.save()
            else:
                new_name = City.objects.create(name=name)
                new_name.save()
        except:
            return render(request, 'weather_app/index.html',{'message':'invalid data'})

    cities = City.objects.all().order_by("-id")[:4]
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city,api_key)).json()
        weather = {
        'city': city,
        'temprature': round((city_weather['main']['temp']-32)*(5/9),2),
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)

    context = {
        'weather_data' : weather_data
    }
    return render(request, 'weather_app/index.html',context)