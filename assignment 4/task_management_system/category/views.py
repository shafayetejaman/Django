from django.shortcuts import render,redirect
from .forms import CategoryForms


# Create your views here.
def index(request):
    if request.method == "POST":
        form = CategoryForms(request.POST)
        if form.is_valid():
            form.save()

            return redirect("home")

    form = CategoryForms()
    return render(request, "category/index.html", {"form": form})
