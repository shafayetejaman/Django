from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "authenticate/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
