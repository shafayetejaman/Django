from django.db import models
from django.contrib.auth.models import User
from 

# Create your models here.


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_bought = models.DateTimeField(auto_now_add=True)
