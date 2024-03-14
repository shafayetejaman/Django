from django.db import models


# Create your models here.
class DBStudent(models.Model):
    name = models.CharField(max_length=50)
    ID = models.IntegerField(primary_key=True)
    email = models.TextField()
    
    def __str__(self) -> str:
        return f"ID: {self.ID} Name: {self.name}"
