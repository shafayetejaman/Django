from django.shortcuts import render
from 
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.
class CreateCarPostView(CreateView):
    model = 