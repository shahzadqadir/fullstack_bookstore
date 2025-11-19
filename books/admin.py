# ~/automation/fullstack_bookstore/books/admin.py

from django.contrib import admin

# Register your models here.

from .models import Book, Author

admin.site.register(Book)
admin.site.register(Author)