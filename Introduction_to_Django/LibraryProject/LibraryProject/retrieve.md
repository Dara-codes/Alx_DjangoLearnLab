# Retrieve the book you just created

retrieved_book = Book.objects.filter(title="1984").first()
print(retrieved_book)

# Document in retrieve.md

with open('retrieve.md', 'w') as file:
file.write(f"Command: Retrieve and display all attributes of the book you just created.\n")
file.write(f"Output: {retrieved_book}\n")
