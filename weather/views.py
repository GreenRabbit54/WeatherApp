import city as city
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    app_id = '4c58f17d50188460de439e217600ff3c'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'info':all_cities, 'form':form}
    return render(request,'weather/index.html', context)