from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def books(request):
    template = 'books.html'
    all_books = Book.objects.all()
    context = {'books': all_books}
    return render(request, template, context)

def pub_date(request):
    template = 'pub_date.html'
    books = Book.objects.filter(name='Война и мир')
    context = {'books': books}
    return render(request, template, context)