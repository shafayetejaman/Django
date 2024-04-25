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
    success_url = reverse_lazy("post_list")

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
    success_url = reverse_lazy("post_list")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class DeletePostView(DeleteView):
    model = Car
    pk_url_kwarg = "id"
    template_name = "show_cars/delete_post.html"
    success_url = reverse_lazy("post_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class UpdatePostView(UpdateView):
    model = Car
    form_class = CarForm
    pk_url_kwarg = "id"
    template_name = "show_cars/Update_post.html"
    success_url = reverse_lazy("post_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context