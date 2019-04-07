import requests

from django.shortcuts import render,HttpResponse
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8cebd01baccaedf377ffab6d466444ea'

    if request.method == 'POST':
        form = CityForm(request.POST)

        city1 = request.POST['name']

        form.save()
        #
        #
        cities = list(City.objects.filter(name=city1))


        weather_data = []


        for city in cities:

            r = requests.get(url.format(city)).json()
            print(r)
            city_weather = {
                'city' : city.name,
                'temperature' : r['main']['temp'],
                    'description' : r['weather'][0]['description'],
                    'icon' : r['weather'][0]['icon'],
                }

            weather_data.append(city_weather)
        del weather_data[1:]
        context = {'weather_data' : weather_data, 'form' : form}
        return render(request, 'cityw/weather.html', context)
    else:
        form = CityForm()
        context = {'form': form}
        return render(request, 'cityw/weather.html', context)




# def index(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8cebd01baccaedf377ffab6d466444ea'
#
#
#     form = CityForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#
#         city = City.objects.filter(name='name')
#         print(city)
#         r = requests.get(url.format(city.name)).json()
#
#         weather_data = {
#             'city' : city.name,
#             'temperature' : r['main']['temp'],
#             'description' : r['weather'][0]['description'],
#             'icon' : r['weather'][0]['icon'],
#         }
#
#
#
#         context = {'weather_data' : weather_data,'form':form}
#         return render(request, 'cityw/weather.html', context)
#
#     return render(request, 'cityw/weather.html')
#


