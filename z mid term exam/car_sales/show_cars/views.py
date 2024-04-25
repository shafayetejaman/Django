from django.shortcuts import render
from .models import Brand,Car,Comment
from .forms import BrandForm,CarForm,CommentForm
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.
class CreateCarPostView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "show_cars/make_car.html"
    success_url = reverse_lazy()