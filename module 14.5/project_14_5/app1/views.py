from django.shortcuts import render
from app1.forms import MyForm, MyDBForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            file = data["profile_img"]
            with open("./app1/static/app1/images/" + file.name, "wb+") as des:
                for i in file.chunks():
                    des.write(i)

            form = MyForm()
            return render(
                request,
                "app1/index.html",
                {"form": form, "data": data},
            )

    form = MyForm()
    return render(request, "app1/index.html", {"form": form})


def db(request):
    if request.method == "POST":
        form = MyDBForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            form.save()
            form = MyDBForm()
            return render(
                request,
                "app1/dbpage.html",
                {"form": form, "data": data},
            )

    form = MyDBForm()
    return render(request, "app1/dbpage.html", {"form": form})
