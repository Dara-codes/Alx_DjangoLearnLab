from django.contrib import admin

# Register your models here.
from relationship_app.models import Author, Book, Library

# Create some authors
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")

# Create some books
book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1, publication_year=1997)
book2 = Book.objects.create(title="1984", author=author2, publication_year=1949)
book3 = Book.objects.create(title="Animal Farm", author=author2, publication_year=1945)

library = Library.objects.create(name="Central Library")
library.books.add(book1, book2, book3)

