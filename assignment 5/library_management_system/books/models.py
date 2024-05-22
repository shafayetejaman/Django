from django.db import models

# Create your models here.
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    # title, description,image, borrowing price, user reviews
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField()
    price = models.FloatField()
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
