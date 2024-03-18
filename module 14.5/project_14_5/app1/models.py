from django.db import models

# Create your models here.
class MyDBForm(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.IntegerField()