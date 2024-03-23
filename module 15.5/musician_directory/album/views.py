from django.shortcuts import render
from .forms import albums


# Create your views here.
def index(request):
    if request.method == "POST":
        form = albums(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            form = albums()
            return render(
                request,
                "album/index.html",
                {"form": form, "data": data},
            )

    form = albums()
    return render(request, "album/index.html", {"form": form})
