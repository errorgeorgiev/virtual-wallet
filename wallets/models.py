from django.db import models
from django.contrib.auth.models import AbstractUser
import bitcoin

# Create your models here.

class Transaction(models.Model):
    name = models.CharField(max_length=32)
    current_price = models.DecimalField(max_digits=20, decimal_places=3)
    quantity = models.IntegerField(default=0)

class CustomUser(AbstractUser):
    coins = models.ManyToManyField(Transaction)

    def __str__(self): 
        return self.email 