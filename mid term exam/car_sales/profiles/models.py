from django.db import models

# Create your models here.


class History(models.Model):
    user_id = models.IntegerField()
    car_id = models.IntegerField()
    date_bought = models.DateTimeField(auto_now_add=True)
