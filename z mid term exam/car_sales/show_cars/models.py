from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    
    
class Car(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    slug = models.SlugField(max_length=100,unique=True)
    bland = models.
