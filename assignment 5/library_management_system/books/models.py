from django.db import models

# Create your models here.
class Book(models.Model):
    # title, description,image, borrowing price, user reviews
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()

