from django.db import models
from musician.models import musicians


# Create your models here.
class albums(models.Model):
    choice = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    album_name = models.CharField(max_length=20)
    release_date = models.DateField()
    rating = models.CharField(choices=choice, max_length=50, null=True, blank=True)
    musician = models.ForeignKey(musicians, on_delete=models.CASCADE)
