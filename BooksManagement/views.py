from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'BooksManagement/books_list.html', context)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')

    else:
        form = BookForm()
    return render(request, 'BooksManagement/book_create.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'BooksManagement/book_update.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book:book_list')
    return render(request, 'BooksManagement/book_delete.html', {'book': book})
