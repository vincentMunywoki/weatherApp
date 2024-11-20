import urllib.request  # help us in sending and accepting requests from our APIs
import json 
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=a04cc63d5a4ca8b3e3714bc42616cb41').read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
        }

    