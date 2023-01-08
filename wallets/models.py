from django.db import models
from django.contrib.auth.models import AbstractUser
import bitcoin

# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=32)
    symbol = models.CharField(max_length=8)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    quantity = models.IntegerField(default=0)
    market_cap = models.DecimalField(max_digits=20, decimal_places=3)
    percent_change = models.DecimalField(max_digits=6, decimal_places=2)

class CustomUser(AbstractUser):
    wallet_address = models.CharField(max_length=64, default=bitcoin.random_key())
    coins = models.ManyToManyField(Coin)

    def __str__(self): 
        return self.email 