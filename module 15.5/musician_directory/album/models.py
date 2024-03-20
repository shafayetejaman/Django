from django.db import models


# Create your models here.
class albums(models.Model):
    album_name = models.CharField(max_length=20)
    release_date = models.DateField()
    rating = models.CharField(null=True, default=None)
