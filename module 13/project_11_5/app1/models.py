from django.db import models

# Create your models here.
class DBStudent(models.Model):
    name = models.CharField(max_length=50)
    _id = models.IntegerField(primary)