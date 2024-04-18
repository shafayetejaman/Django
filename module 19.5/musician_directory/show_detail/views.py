from django.shortcuts import render
from album.models import albums


# Create your views here.
def index(request):
    data = albums.objects.all()
    print(data)
    return render(request, "show_detail/index.html", {"data": data})
