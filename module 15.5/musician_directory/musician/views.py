from django.shortcuts import render
from .forms import musicians_forms          


# Create your views here.
def index(request):
    if request.method == "POST":
        form = album_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            form = album_forms()
            return render(
                request,
                "album/index.html",
                {"form": form, "data": data},
            )

    form = album_forms()
    return render(request, "album/index.html", {"form": form})
