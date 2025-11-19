# ~/automation/fullstack_bookstore/books/views.py

from django.shortcuts import render, redirect   
from django.urls import reverse                 

from .models import Book, Author
from .forms import UpdateForm   # NEW import

# Create your views here.

def books_home(request):
    return render(request, 'books/index.html')

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})

def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book_detail.html', {'book': book})

def book_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(reverse('books_list'))

def book_update(request, id):   # NEW
    current_book = Book.objects.get(id=id)
    form = UpdateForm(instance=current_book)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=current_book)
        if form.is_valid():
            form.save()
            return redirect(reverse('books_list'))
    return render(request, 'books/book_update.html', {'form': form})
