from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    account_no = models.IntegerField(
        unique=True
    )  # account no duijon user er kokhono same hobe na
    birth_date = models.DateField(null=True, blank=True)
