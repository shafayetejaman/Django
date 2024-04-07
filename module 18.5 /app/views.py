from django.shortcuts import render
from .forms import Re

# Create your views here.
def index(request):
    return render(request, "app/index.html")