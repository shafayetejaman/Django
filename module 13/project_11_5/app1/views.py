from django.shortcuts import render
from . django_forms import StudentForm
# Create your views here.


def index(request):
    return render(request, "app1/index.html")

def result(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        print(form.changed_data)
        return render(request, "app1/result.html", )
