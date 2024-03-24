from django.shortcuts import render
from .forms import album_forms
from .models import albums

# Create your views here.
def index(request):
    if request.method == "POST":
        form = album_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            form.save()
            print(data)

            form = album_forms()
            return render(
                request,
                "album/index.html",
                {"form": form, "data": data},
            )

    form = album_forms()
    return render(request, "album/index.html", {"form": form})

def edit(request, id):
    model_data = albums.objects.get(pk=id)
    form = album_forms(request.PO) 
    
    if request.method == "POST":
        form = album_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            form.save()
            print(data)

            form = album_forms()
            return render(
                request,
                "album/index.html",
                {"form": form, "data": data},
            )

    form = album_forms()
    return render(request, "album/index.html", {"form": form})