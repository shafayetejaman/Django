from django.shortcuts import render
from .forms import Register


# Create your views here.
def index(request):
    if request.method == "POST":
        form = Register(request.POST)

    form = Register()
    return render(request, "app/index.html", {"form": form})
