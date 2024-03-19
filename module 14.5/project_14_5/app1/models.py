from django.db import models


# Create your models here.
class MyDBFormClass(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    balance = models.BigIntegerField()
    login = models.BooleanField(default=True)
    about = models.TextField(max_length=50)
