from django.shortcuts import render
from album.models import albums


# Create your views here.
def index(request):
    data = albums.objects.get()

    return render(request, "show_detail/index.html", {"data": data})
