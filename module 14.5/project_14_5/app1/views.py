from django.shortcuts import render
from app1.forms import MyForm

# Create your views here.
def index(request):
    
    return render(request, "app1/index.html")
