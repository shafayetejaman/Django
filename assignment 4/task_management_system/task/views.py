from django.shortcuts import render, redirect
from .forms import TaskForms

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
