from django.shortcuts import render, redirect
from .models import Book, Comment, Brand
from .forms import BookForm, CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from profiles.models import History


# Create your views here.


def home(request, brand_slug=None):
    books = Book.objects.all()
    brands = Brand.objects.all()
    brand = None

    if brand_slug:
        brand = Brand.objects.get(slug=brand_slug)
        books = Book.objects.filter(brand=brand)

    return render(
        request,
        "show_books/show_post_list.html",
        {
            "logged": request.user.is_authenticated,
            "books": books,
            "brands": brands,
            "current_brand": brand,
        },
    )


class CreatePostView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "show_books/add_post.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().is_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class DetailPostView(DetailView):
    model = Book
    pk_url_kwarg = "id"
    template_name = "show_books/detail_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        comments = book.comments.all().order_by("created").reverse()
        comment_form = CommentForm()

        context["logged"] = self.request.user.is_authenticated
        context["comments"] = comments
        context["comment_form"] = comment_form

        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        book = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()

        return self.get(request, *args, **kwargs)


class DeletePostView(DeleteView):
    model = Book
    pk_url_kwarg = "id"
    template_name = "show_books/delete_post.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


class UpdatePostView(UpdateView):
    model = Book
    form_class = BookForm
    pk_url_kwarg = "id"
    template_name = "show_books/Update_post.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged"] = self.request.user.is_authenticated
        return context


def buy_book(request, id):
    book = Book.objects.get(pk=id)
    book.quantity -= 1
    book.save()

    History.objects.create(book=book, user=request.user)

    return redirect("home")
