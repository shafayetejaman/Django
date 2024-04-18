from django.shortcuts import render, redirect
from .forms import album_forms
from .models import albums
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def index(request):
    if request.method == "POST":
        form = album_forms(request.POST)
        if form.is_valid():
            form.save()

            return redirect("show")

    form = album_forms()
    return render(request, "album/index.html", {"form": form})


class IndexFormView(CreateView):
    model = albums
    form_class = album_forms
    template_name = "album/index.html"
    success_url = reverse_lazy("show")

    def form_valid(self, form):
        return super().form_valid(form)


def edit(request, id):
    model_data = albums.objects.get(pk=id)
    form = album_forms(instance=model_data)

    if request.method == "POST":
        form = album_forms(request.POST, instance=model_data)
        if form.is_valid():
            form.save()

            return redirect("show")

    return render(request, "album/index.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class EditFromView(UpdateView):
    model = albums
    form_class = album_forms
    template_name = "album/index.html"
    success_url = reverse_lazy("show")
    pk_url_kwarg = "id"


def delete(request, id):
    model_data = albums.objects.get(pk=id)
    model_data.delete()

    return redirect("show")


@method_decorator(login_required, name="dispatch")
class DeleteFromView(DeleteView):
    model = albums
    template_name = "album/delete.html"
    success_url = reverse_lazy("show")
    pk_url_kwarg = "id"
