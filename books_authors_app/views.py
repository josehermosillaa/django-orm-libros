from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def create_book(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/books')



