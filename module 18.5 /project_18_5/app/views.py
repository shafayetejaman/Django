from django.shortcuts import render, redirect
from .forms import Register
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def user_signup(request):
    if request.user.is_authenticated:
        redirect("home")
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            form = Register()
        else:
            messages.warning(request, "Account Creation Failed!")

    return render(request, "app/index.html", {"form": form})


def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username, password)

            if user is not None:
                login(request, user)
                return redirect("home")
        else:
            messages.warning(request, "Login Failed!")

    return render(request, "app/index.html", {"form": form})


def home(request):
    if request.user.is_authenticated:
        return render(request, "app/home.html", {"user": request.user})

    return redirect("signup")
