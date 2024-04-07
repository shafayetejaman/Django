from django.shortcuts import render
from .forms import Register


# Create your views here.
def index(request):
    form = Register()

    return render(request, "app/index.html", {"form": form})
