from django.db import models

# Create your models here.
class Book(models.Model):
    # title, description,image, borrowing price, user reviews
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField()
    price = models.FloatField()
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
