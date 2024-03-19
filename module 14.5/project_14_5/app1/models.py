from django.db import models


# Create your models here.
class MyDBFormClass(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

