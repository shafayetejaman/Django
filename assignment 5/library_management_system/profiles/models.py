from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    parched = models.DateTimeField(auto_now_add=True)
