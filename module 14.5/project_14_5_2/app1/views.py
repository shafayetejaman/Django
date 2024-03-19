from django.shortcuts import render

from . import forms


# Create your views here.
def db(request):
    if request.method == "POST":
        form = forms.MyDBForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            form.save()
            print(data)

            form = forms.MyDBForm()
            return render(
                request,
                "app1/dbpage.html",
                {"form": form, "data": data},
            )

    form = forms.MyDBForm()
    return render(request, "app1/dbpage.html", {"form": form})
