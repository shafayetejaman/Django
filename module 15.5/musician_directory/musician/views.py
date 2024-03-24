from django.shortcuts import render, redirect
from .forms import musicians_forms


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
