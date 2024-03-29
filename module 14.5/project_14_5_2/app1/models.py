from django.db import models


# Create your models here.
class MyDBFormClass(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    balance = models.IntegerField(blank=True, null=True)
    login = models.BooleanField(default=True)
    about = models.TextField(max_length=50)
    date = models.DateField()
    hour_rate = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField()
    profile_img = models.FileField(upload_to="app1/static/app1/upload/")
    website = models.URLField()
