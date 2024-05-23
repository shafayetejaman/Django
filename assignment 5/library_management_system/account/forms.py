from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        
        if commit:
            UserAccount.objects.create(
                user=user
            )
            user.save()
        
        return user