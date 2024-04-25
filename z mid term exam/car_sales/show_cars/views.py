from django.shortcuts import render
from .models import Car, Comment
from .forms import CarForm, CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


# Create your views here.


class CreatePostView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "show_cars/add_post.html"
    success_url = reverse_lazy("show")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().is_valid(form)


class DetailPostView(DetailView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "show_cars/show_post_list.html"
    success_url = reverse_lazy("show")


class DeletePostView(DeleteView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "show_cars/delete_post.html"
    success_url = reverse_lazy("show")


class UpdatePostView(UpdateView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "show_cars/Update_post.html"
    success_url = reverse_lazy("show")
