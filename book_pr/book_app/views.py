from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm, DeleteConfirmForm

from .forms import UpdateBookForm, DeleteBookForm


def index(request):
    return render(request, 'book_app/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_app/book_list.html', {'books': books})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    book.views += 1
    book.save()
    return render(request, 'book_app/book_detail.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'book_app/add_book.html', {'form': form})

# views.py


def update_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', slug=book.slug)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_app/update_book.html', {'form': form, 'book': book})

def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = DeleteBookForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            book.delete()
            return redirect('book-list')
    else:
        form = DeleteBookForm()
    return render(request, 'book_app/delete_book.html', {'form': form, 'book': book})



