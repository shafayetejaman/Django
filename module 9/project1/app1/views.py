from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    d = {"items" : {"shope" : 50,
         "oil" : 300,
         "fruit" : 30}
         }
    return render(request, "app1/index.html", d)
