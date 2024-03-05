from django.shortcuts import render
from templates import index

# Create your views here.

def index(request):
    return render(request, index())
