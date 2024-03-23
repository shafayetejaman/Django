from django.db import models


# Create your models here.
class musicians(models.Model):
    choice = [
        ("guitar", "Guitar"),
        ("piano", "Piano"),
        ("drums", "Drums"),
        ("violin", "Violin"),
        ("flute", "Flute"),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    instrument_type = models.CharField(max_length=50, choices=choice, null=True,blank=True)
