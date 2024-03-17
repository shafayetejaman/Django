from django.shortcuts import render
from app1.forms import MyForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, "app1/index.html", {})

    return render(request, "app1/index.html", {"form": form})
