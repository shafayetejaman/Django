from django.shortcuts import render, redirect
from .models import Car, Comment
from .forms import CarForm, CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


# Create your views here.


def home(request, id):
    data = Car.objects.all()
    brand = 
    return render(
        request,
        "show_cars/show_post_list.html",
        {"logged": request.user.is_authenticated, "cars": data},
    )


class CreatePostView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "show_cars/add_post.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().is_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class DetailPostView(DetailView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "show_cars/detail_post.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class DeletePostView(DeleteView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "show_cars/delete_post.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class UpdatePostView(UpdateView):
    model = Car
    form_class = CarForm
    pk_url_kwarg = "id"
    template_name = "show_cars/Update_post.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


def buy_car(request, id):
    car = Car.objects.get(pk=id)
    car.quantity -= 1
    car.save()
    return redirect("home")
