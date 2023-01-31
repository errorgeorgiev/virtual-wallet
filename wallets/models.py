from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=32)
    current_price = models.FloatField() # new
    average_price = models.FloatField() # new
    quantity = models.IntegerField(default=0)

class Transaction(models.Model):
    type = models.CharField(max_length=32)
    date = models.DateTimeField()
    coin_name = models.CharField(max_length=32)
    quantity = models.FloatField() # new, was integer
    price_when_bought = models.FloatField()

    def __str__(self):
        return self.coin_name

class CustomUser(AbstractUser):
    total_deposits = models.IntegerField(default = 0) # new
    current_account_value = models.FloatField(default=0.0) # new
    coins = models.ManyToManyField(Coin)
    transactions = models.ManyToManyField(Transaction)

    def __str__(self): 
        return self.email 