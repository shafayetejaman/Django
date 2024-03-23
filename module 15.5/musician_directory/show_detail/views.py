from django.shortcuts import render
from album.forms import musicians_forms


# Create your views here.
def index(request):
    if request.method == "POST":
        form = musicians_forms(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            form = musicians_forms()
            return render(
                request,
                "musician/index.html",
                {"form": form, "data": data},
            )

    form = musicians_forms()
    return render(request, "musician/index.html", {"form": form})
