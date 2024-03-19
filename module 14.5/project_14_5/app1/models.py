from django.db import models


# Create your models here.
class MyDBForm(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, min_length=3)
