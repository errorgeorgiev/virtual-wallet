from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CryptoForm


# Create your views here.
from django.views.generic import TemplateView
import requests

def success_view(request, crypto):
    return render(request, 'success.html', {'crypto' : crypto})

def trade_view(request):
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        if form.is_valid():
            crypto = form.cleaned_data['crypto']
            quantity = form.cleaned_data['quantity']
        return redirect('success_view', crypto=crypto)

    else:
        form = CryptoForm()
        return render(request, 'trade.html', {'form' : form})

def portfolio_view(request):
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily').json()


    return render(request, 'portfolio.html', {'api_data': api_data})

def home_view(request):
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false').json()
    
    return render(request, 'home.html', {'api_data': api_data})

class HomePageView(TemplateView):
    template_name = 'home.html'

