from django.shortcuts import render
from .django_forms import StudentForm

# Create your views here.


def index(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "app1/index.html", {"form": form})


def result(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        return render(request, "app1/result.html", form.cleaned_data)

    return render(request, "app1/result.html")
