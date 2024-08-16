from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Avg

from .models import Book

# Create your views here.
books = Book.objects.all().order_by("title")
num_books = books.count()
avg_rating = books.aggregate(Avg("rating"))
def index(request):
    return render(request, "book_outlet/index.html", {
    "books": books,
    "Total_no_of_books": num_books,
    "Average_Rating": avg_rating

    })

def book_details(request, slug):
    book =get_object_or_404(Book, slug = slug)
    return render(request, "book_outlet/book_details.html", {
        "title": book.title,
        "author": book.author,
        "rating" :book.rating,
        "is_bestselling" : book.is_bestselling

    })

