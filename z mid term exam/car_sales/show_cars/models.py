from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()

class Brand(models.Model):
    name = models.CharField(max_length=20)
    