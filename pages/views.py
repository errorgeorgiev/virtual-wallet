from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
from django.views.generic import TemplateView
import requests


def home_view(request):
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false').json()
    
    return render(request, 'home.html', {'api_data': api_data})

class HomePageView(TemplateView):
    template_name = 'home.html'