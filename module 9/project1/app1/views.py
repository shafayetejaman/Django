from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    d = {'author' : 'Rahim', 'age' : 5}
    return render(request, "app1/index.html", d)
