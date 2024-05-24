from django.shortcuts import render,redirect
from profiles.models import History
from books.models import Book

# Create your views here.


def buy_book(request, id):
    book = Book.objects.get(pk=id)
    book.save()

    History.objects.create(book=book, user=request.user)

    return redirect("home")
