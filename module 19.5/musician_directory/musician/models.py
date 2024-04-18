from django.db import models


# Create your models here.
class musicians(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    instrument_type = models.TextField(max_length=50, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.first_name}"
