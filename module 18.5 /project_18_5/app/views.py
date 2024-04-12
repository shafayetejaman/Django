from django.shortcuts import render
from .forms import Register
from django.contrib import messages

# Create your views here.


def index(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)
        messages.success(request, "Account Created Successfully!")
        # messages.warning(request, "Account Not Creation Failed!")
        # messages.info(request, "Account INFO!")

        if form.is_valid():
            form.save()
            form = Register()

    return render(request, "app/index.html", {"form": form})
