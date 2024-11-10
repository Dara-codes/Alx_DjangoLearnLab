import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    author1 = Author.objects.create(name='Author 1')
    author2 = Author.objects.create(name='Author 2')

    book1 = Book.objects.create(title='Book 1', author=author1)
    book2 = Book.objects.create(title='Book 2', author=author1)
    book3 = Book.objects.create(title='Book 3', author=author2)

    library1 = Library.objects.create(name='Library 1')
    library2 = Library.objects.create(name='Library 2')

    library1.books.add(book1, book2)
    library2.books.add(book3)

    librarian1 = Librarian.objects.create(name='Librarian 1', library=library1)
    librarian2 = Librarian.objects.create(name='Librarian 2', library=library2)

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

if __name__ == "__main__":
    create_sample_data()

    author_name = 'Author 1'
    books_by_author = query_books_by_author(author_name)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    library_name = 'Library 1'
    books_in_library = query_books_in_library(library_name)
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    librarian_for_library = query_librarian_for_library(library_name)
    print(f"Librarian for {library_name}: {librarian_for_library.name}")
