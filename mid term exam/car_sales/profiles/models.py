from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class History(models.Model):
    user = models.IntegerField()
    car_id = models.IntegerField()
    date_bought = models.DateTimeField(auto_now_add=True)
