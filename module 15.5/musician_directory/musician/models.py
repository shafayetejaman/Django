from django.db import models
choice = [
    ("guitar", "Guitar"),
    ("piano", "Piano"),
    ("drums", "Drums"),
    ("violin", "Violin"),
    ("flute", "Flute"),
]

# Create your models here.
class musicians(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    instrument_type = models.CharField(max_length=50, choices=choice, d)
