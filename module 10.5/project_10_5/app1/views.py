from django.shortcuts import render

# Create your views here.


def home(request):
    data = [
        {"id": 1, "name": ["Introduction", "to", "Python"], "fee": 5000},
        {"id": 2, "name": ["Introduction", "to", "Django"], "fee": 10000},
        {"id": 3, "name": ["Introduction", "to", "c++"], "fee": 1000},
        {"id": 4, "name": ["Introduction", "to", "Java"], "fee": 2000},
        {"id": 5, "name": ["Introduction", "to", "C#"], "fee": 3000},
    ]

    return render(request, "app1/home.html", {"course": data})
