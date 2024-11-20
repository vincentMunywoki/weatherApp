import urllib.request  # help us in sending and accepting requests from our APIs
import json 
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
    