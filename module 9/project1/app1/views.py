from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    d = {a:12}
    return render(request, "app1/index.html")
