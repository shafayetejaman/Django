from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserChangeForm


# Create your views here.


@method_decorator(login_required, name="dispatch")
class PasswordChangeView(PasswordChangeView):
    template_name = "profiles/pass_change.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Password Updated Successfully!")
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


login_required()


def profile(request):
    data = request.user
    return render(request, "profiles/profile.html", {"data": data, "logged":request.user.is_authenticated})


class UserUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "profiles/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
