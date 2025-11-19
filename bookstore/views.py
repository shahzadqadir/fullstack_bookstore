# ~/automation/fullstack_bookstore/bookstore/views.py

from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("<h1>Hello, World</h1>")

def custom_hello_world(request, name):
    return HttpResponse(f"<h1>Hello, {name}")