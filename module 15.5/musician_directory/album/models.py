from django.db import models
from .


# Create your models here.
class albums(models.Model):
    album_name = models.CharField(max_length=20)
    release_date = models.DateField()
    rating = models.CharField(default=None)
    musician = models.ForeignKey(musician, on_delete=models.CASCADE)
