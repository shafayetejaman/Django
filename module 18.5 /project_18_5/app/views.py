from django.shortcuts import render
from .forms import Register
from django.contrib import messages
from django.contrib.auth import authenticate, logout,login

# Create your views here.


def index(request):
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

def 