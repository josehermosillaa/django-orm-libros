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

def show_book(request,book_id):
    book = Book.objects.get(id = book_id)
    context = {
        'book':book,
        'authors': Author.objects.exclude(books__id = book_id)
    }

    return render(request, 'book.html',context)

def assign_book(request,book_id):
    book = Book.objects.get(id = book_id)
    author = Author.objects.get(id =request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}')

def assign_author(request, author_id):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = author_id)
    book.authors.add(author)
    return redirect((f'/authors/{author_id}'))

def authors(request):
    context = { 
        'authors':Author.objects.all()
    }
    return render(request,'authors.html',context)

def create_author(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name= request.POST['last_name'],notas=request.POST['notas'])
    return redirect('/authors')

def show_author(request, author_id):
    author = Author.objects.get(id = author_id)
    context = {
        'author': Author.objects.get(id = author_id),
        'books': Book.objects.exclude(authors__id = author_id)
    }

    return render(request, 'author.html', context)

def delete_author(request, author_id):
    this_author = Author.objects.get(id = author_id)
    this_author.delete()
    return redirect('/authors')

def delete_book(request, book_id):
    this_book = Book.objects.get(id = book_id)
    this_book.delete()
    return redirect('/books')
    

# def delete_author(request, author_id):
#     this_author = Author.objects.get(id = author_id)
#     this_books = Book.objects.filter(authors__id = author_id)
#     for a in this_books:
#         this_author.books.remove(a.id)
#     return redirect('/authors')

# def delete_book(request, book_id):
#     this_author = Author.objects.filter(books__id = book_id)
#     this_book = Book.objects.get(id = book_id)
#     this_book.authors.remove(this_author)
#     return redirect('/books')






