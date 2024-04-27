from django.db import models
from show_cars.models import Car
from django.contrib.auth.models import User
# Create your models here.

class history(models.Model):
    user = User
    