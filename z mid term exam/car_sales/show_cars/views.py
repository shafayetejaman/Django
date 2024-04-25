from django.shortcuts import render
from .models import Brand,Car,Comment
from .forms import BrandForm,CarForm,CommentForm
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.
class CreateCarPostView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "show"