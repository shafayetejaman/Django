from django.db import models


class Choice(models.Model):
    name = models.CharField(max_length=100)


# Create your models here.
class musicians(models.Model):
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    instrument_type = models.ManyToManyField(Choice)
