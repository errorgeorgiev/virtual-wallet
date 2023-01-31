from django import forms
import requests

class CryptoForm(forms.Form):
    api_data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false').json()
    CRYPTO_CHOICES = []
    for item in api_data:
        CRYPTO_CHOICES.append((item['name'], item['name']))


    crypto = forms.ChoiceField(choices=CRYPTO_CHOICES)
    quantity = forms.DecimalField()


class DepositForm(forms.Form):
    value = forms.DecimalField()
    currency = 'USD'