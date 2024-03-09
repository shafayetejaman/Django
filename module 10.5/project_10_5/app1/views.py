from django.shortcuts import render

# Create your views here.


def home(request):
    data = [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000 
        },
        {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000 
        },
        {
            'id' : 4,
            'name' : 'C++',
            'fee' : 2000 
        },
        {
            'id' : 5,
            'name' : 'C#',
            'fee' : 3000 
        },
    ]

    return render(request, "app1/home.html", {"course": data})
