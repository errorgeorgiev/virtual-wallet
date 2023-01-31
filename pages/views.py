from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CryptoForm, DepositForm
from wallets.models import CustomUser, Transaction


# Create your views here.
from django.views.generic import TemplateView
import requests


def success_deposit_view(request, value):
    return render(request, 'success_deposit.html', {'value' : value})

def success_buy_view(request, crypto):
    return render(request, 'success_buy.html', {'crypto' : crypto})

def success_sell_view(request, crypto):
    return render(request, 'success_sell.html', {'crypto' : crypto})

def trade_view(request):
    # last year data
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365&interval=daily').json()
    year_data = []
    for item in api_data['prices']:
        year_data.append(item[1])

    # last month data
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily').json()
    month_data = []
    for item in api_data['prices']:
        month_data.append(item[1])

    # last week data
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7&interval=hourly').json()
    week_data = []
    for item in api_data['prices']:
        week_data.append(item[1])

    # last day data
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1&interval=hourly').json()
    day_data = []
    for item in api_data['prices']:
        day_data.append(item[1])
    
    data = {
        'year_data' : year_data,
        'month_data' : month_data,
        'week_data' : week_data,
        'day_data' : day_data,
    }
    return render(request, 'trade.html', {'data' : data})

def buy_view(request):
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        if form.is_valid():
            # user = request.user
            crypto = form.cleaned_data['crypto']
            # quantity = form.cleaned_data['quantity']
            # data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false').json()
            # for item in data:
            #     if item['name'] == crypto:
            #         price = item['current_price']
            # transaction, created = Transaction.objects.get_or_create(name=crypto, quantity=quantity, current_price=price)
            # user.coins.add(transaction)
        return redirect('success_buy_view', crypto=crypto)

    else:
        form = CryptoForm()
        return render(request, 'buy.html', {'form' : form})


def sell_view(request):
    if request.method == 'POST':
        form = CryptoForm(request.POST)
        if form.is_valid():
            #user = request.user
            crypto = form.cleaned_data['crypto']
            # quantity = form.cleaned_data['quantity']
            # data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false').json()
            # for item in data:
            #     if item['name'] == crypto:
            #         price = item['current_price']
            # transaction, created = Transaction.objects.get_or_create(name=crypto, quantity=quantity, current_price=price)
            # user.coins.add(transaction)
        return redirect('success_sell_view', crypto=crypto)

    else:
        form = CryptoForm()
        return render(request, 'sell.html', {'form' : form})

def deposit_view(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
        return redirect('success_deposit_view', value=value)

    else:
        form = DepositForm()
        return render(request, 'deposit.html', {'form' : form})


def portfolio_view(request):
    username = 'admin'
    email = 'admin@admin.com'
    entry_values = [1, 2, 300, 1000, 10000]
    entry_coins = [ "bitcoin", "ethereum", "cardano", "doge", "xrp" ]
    # prices = pass // maybe should be updated in the fist page
    deposited_amount = 100000
    current_amount = 120000
    values = []
    coins = []

    for i in range (5):
        values.append(entry_coins[i])
        coins.append(entry_values[i])
    
    data = {
        'username' : username,
        'email' : email,
        'values' : values,
        'coins' : coins,
        # 'prices' : prices
        'deposited_amount' : deposited_amount,
        'current_amount' : current_amount,
    }
    
    return render(request, 'portfolio.html', {'data': data})

def home_view(request):
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false').json()
    
    return render(request, 'home.html', {'api_data': api_data})

class HomePageView(TemplateView):
    template_name = 'home.html'

