from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)

        current_date = datetime.now()
        date = int(current_date.strftime("%Y%m%d"))

        if commit:
            user.save()
            UserAccount.objects.create(user=user, account_no=date + user.id)

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
