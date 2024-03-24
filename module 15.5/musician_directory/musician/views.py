from django.shortcuts import render, redirect
from .forms import musicians_forms
from .models import musicians


# Create your views here.
def index(request):
    if request.method == "POST":
        form = musicians_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            form.save()
            print(data)

            form = musicians_forms()
            return redirect("show")

    form = musicians_forms()
    return render(request, "musician/index.html", {"form": form})


def edit(request, id):
    model_data = albums.objects.get(pk=id)
    form = album_forms(request.POST, instance=model_data)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("show")

    return render(request, "album/index.html", {"form": form})
