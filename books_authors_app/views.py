from django.shortcuts import render, HttpResponse
from .models import *

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)



