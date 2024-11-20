from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Book
from .forms import BookForm
from django.db.models import Q
from django.utils.html import escape
from django.core.exceptions import ValidationError
from .forms import BookSearchForm, BookForm
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .forms import ExampleForm

@login_required
@csrf_protect
@require_http_methods(["GET"])
def book_list(request):
    """Secure view for listing books with safe search functionality."""
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        if search_query:
            # Use Django's ORM for safe querying instead of raw SQL
            books = books.filter(
                Q(title__icontains=search_query) |
                Q(author__icontains=search_query)
            )

    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'form': form
    })

@login_required
@csrf_protect
@require_http_methods(["GET", "POST"])
def book_create(request):
    """Secure view for creating new books."""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                book = form.save(commit=False)
                book.created_by = request.user
                book.clean()  # Additional validation
                book.save()
                return redirect('book_list')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = []
    
    if form.is_valid():
        query = form.cleaned_data.get('query', '')
        books = Book.objects.filter(title__icontains=query)
    
    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'form': form
    })

def example_form_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
