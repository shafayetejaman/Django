from django.db import models

# Create your models here.
class DBStudent(models.Model):
    name = models.CharField(max_length=50)
    ID = models.IntegerField(primary_key=True)
    email = models.cha