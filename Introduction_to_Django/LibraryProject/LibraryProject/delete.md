# Delete the book you created

retrieved_book.delete()

# Confirm deletion

all_books = Book.objects.all()
print(all_books)

# Document in delete.md

with open('delete.md', 'w') as file:
file.write(f"Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.\n")
file.write(f"Output: {list(all_books)}\n")
