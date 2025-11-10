# ~/automation/fullstack_bookstore/bookstore/urls.py

from django.contrib import admin
from django.urls import path, include    # NEW Import , include

from .views import hello_world, custom_hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world, name='hello_world'),
    path('custom/<str:name>/', custom_hello_world, name='custom_hello_world'),
    path('books/', include('books.urls')),      # NEW
]