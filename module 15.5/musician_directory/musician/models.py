from django.db import models


# Create your models here.
class musicians(models.Model):
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField(va)
