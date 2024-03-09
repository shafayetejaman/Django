from django.shortcuts import render

# Create your views here.


def home(request):
    books = [
        {
            "ID": 1,
            "Title": "The Great Gatsby",
            "Author": "F. Scott Fitzgerald",
            "Genre": "Fiction",
            "Year Published": 1925,
        },
        {
            "ID": 2,
            "Title": "To Kill a Mockingbird",
            "Author": "Harper Lee",
            "Genre": "Fiction",
            "Year Published": 1960,
        },
        {
            "ID": 3,
            "Title": "1984",
            "Author": "George Orwell",
            "Genre": "Dystopian",
            "Year Published": 1949,
        },
        {
            "ID": 4,
            "Title": "Pride and Prejudice",
            "Author": "Jane Austen",
            "Genre": "Romance",
            "Year Published": 1813,
        },
        {
            "ID": 5,
            "Title": "Moby-Dick",
            "Author": "Herman Melville",
            "Genre": "Adventure",
            "Year Published": 1851,
        },
        {
            "ID": 6,
            "Title": "War and Peace",
            "Author": "Leo Tolstoy",
            "Genre": "Historical",
            "Year Published": 1869,
        },
    ]

    return render(request, "app1/home.html", {"data": books})
