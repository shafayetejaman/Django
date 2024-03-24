from django.shortcuts import render,redirect
from .forms import album_forms
from .models import albums


# Create your views here.
def index(request):
    if request.method == "POST":
        form = album_forms(request.POST)
        if form.is_valid():
            form.save()

            return redirect("show")

    form = album_forms()
    return render(request, "album/index.html", {"form": form})


def edit(request, id):
    model_data = albums.objects.get(pk=id)
    form = album_forms(request.POST, instance=model_data)

    if request.method == "POST":
        if form.is_valid():
            form.save()
               
            return redirect("show")

    return render(request, "album/index.html", {"form": form})


def delete(request, id):
    model_data = albums.objects.get(pk=id)
    model_data.delete()
    
    return redirect("show")
