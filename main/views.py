from django.shortcuts import render
from .models import Category, Book


# Create your views here.
def index(request):
    return render(request, 'main/home.html')


def book(request):
    category = Category.objects.all()
    books = Book.objects.all()
    return render(request, 'main/book.html', {'category': category, 'books': books})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')