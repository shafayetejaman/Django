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
from django.contrib.auth.views import LoginView, LogoutView
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


def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
        else:
            messages.warning(request, "Login Failed!")

    return render(request, "authenticate/index.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "authenticate/index.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Login Failed!")
        return super().form_invalid(form)


@method_decorator(login_required, name="dispatch")
class UserLogoutView(LoginView):
    template_name = "authenticate/index.html"
    def get_success_url(self):
        return reverse_lazy("login")


def home(request):
    if request.user.is_authenticated:
        return render(request, "authenticate/home.html", {"user": request.user})

    return redirect("signup")


def user_logout(request):
    logout(request)
    return redirect("login")


def password_change(request):
    if not request.user.is_authenticated:
        return redirect("login")

    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Password Updated Successfully!")
            update_session_auth_hash(request, form.user)
            return redirect("login")

    return render(request, "authenticate/index.html", {"form": form, "pass": True})


def password_change_without(request):
    if not request.user.is_authenticated:
        return redirect("login")

    form = SetPasswordForm(request.user)
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Password Updated Successfully!")
            update_session_auth_hash(request, form.user)
            return redirect("login")

    return render(request, "authenticate/index.html", {"form": form, "pass": True})
