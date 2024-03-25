from django.shortcuts import render, redirect
from .forms import TaskForms
from .models import Task

# Create your views here.
def index(request):
    if request.method == "POST":
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("home")

    form = TaskForms()
    return render(request, "task/index.html", {"form": form})


def edit(request, id):
    model_data = Task.objects.get(pk=id)
    form = TaskForms(instance=model_data)

    if request.method == "POST":
        form = TaskForms(request.POST, instance=model_data)
        if form.is_valid():
            form.save()

            return redirect("home")

    return render(request, "task/index.html", {"form": form})


def delete(request, id):
    model_data = Task.objects.get(pk=id)
    model_data.delete()

    return redirect("home")
