from rest_framework import generics
from .models import Book
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.permissions import IsAuthenticated

# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] 

# Retrieve a single book by its ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()  # To create a book, start with all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()  # Retrieve the books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()  # Get all books
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books



