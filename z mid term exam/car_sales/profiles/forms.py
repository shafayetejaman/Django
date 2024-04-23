from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        exclude = ["password"]
