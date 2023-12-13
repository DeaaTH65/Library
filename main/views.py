from django.shortcuts import render
from .models import Category


# Create your views here.
def index(request):
    category = Category.objects.all()
    return render(request, 'main/home.html', {'category': category})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')