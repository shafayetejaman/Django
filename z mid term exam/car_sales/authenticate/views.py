from django.shortcuts import render, redirect
from .forms import Register
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.


def user_signup(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect("login")
        else:
            messages.warning(request, "Account Creation Failed!")

    return render(request, "authenticate/index.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "authenticate/login.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Login Failed!")
        return super().form_invalid(form)


def user_logout(request):
    logout(request)
    return redirect("login")


class PasswordChangeView(PasswordChangeView):
    template_name = "authenticate/index.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Password Updated Successfully!")
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
