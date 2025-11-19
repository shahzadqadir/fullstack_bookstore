# ~/automation/fullstack_bookstore/books/forms.py

from django import forms

from .models import Book

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"