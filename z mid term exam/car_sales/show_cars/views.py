from django.shortcuts import render
from .models import Brand,Car,Comment
from .forms import CarForm,CommentForm
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.
def show_list(request):
    return render(request, "show_cars/show_list",{"logged":request.user.is_authenticated})

class CreatePostView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "show_cars/make_post.html"
    success_url = reverse_lazy("show")

    def is_valid(self, form):
        form.instance.author = self.request.user
        return super().is_valid(form)
    
class DeletePostView(DetailView):
    model = Car
    form_class = CarForm
    template_name = "show_cars/delete_post.html"
    success_url = reverse_lazy("show")