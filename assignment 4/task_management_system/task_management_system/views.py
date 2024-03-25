from django.shortcuts import render, redirect
from task.models import Task


# Create your views here.
def index(request):
    data = Task.objects.all()

    return render(request, "task/index.html", {"data": data})
