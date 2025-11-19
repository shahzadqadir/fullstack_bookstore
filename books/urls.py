# ~/automation/fullstack_bookstore/books/urls.py

from django.urls import path    
from .views import books_home, books_list, book_details, book_delete, book_update   # NEW import books_update

urlpatterns = [                             
    path('', books_home, name='books_home'),
    path('books_list/', books_list, name='books_list'),     
    path('<int:id>/', book_details, name='book_details'),
    path('<int:id>/delete/', book_delete, name='book_delete'),
    path('<int:id>/update/', book_update, name='book_update'),	# NEW
]