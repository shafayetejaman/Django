from django.shortcuts import render
from app1.forms import MyForm


# Create your views here.
def index(request):
    form = MyForm(request.POST)
    if request == "POST":
        
    return render(request, "app1/index.html", {"form": form})
