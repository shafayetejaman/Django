from django.shortcuts import render
from .forms import Register


# Create your views here.

def index(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            form = Register()
            
    return render(request, "app/index.html", {"form": form})
