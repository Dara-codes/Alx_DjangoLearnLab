from bookshelf.models import Book

# Create a Book instance

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Document in create.md

with open('create.md', 'w') as file:
file.write(f"Command: Create a Book instance with the title '1984', author 'George Orwell', and publication year 1949.\n")
file.write(f"Output: {book}\n")
