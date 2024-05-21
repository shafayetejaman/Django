from django.db import models
from django.contrib.auth.models import User
from books.models import BOOK

# Create your models here.


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(BOOK, on_delete=models.CASCADE)
    parched = models.DateTimeField(auto_now_add=True)
