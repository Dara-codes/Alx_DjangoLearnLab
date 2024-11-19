# Update the title of “1984” to “Nineteen Eighty-Four”

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book)

# Document in update.md

with open('update.md', 'w') as file:
file.write(f"Command: Update the title of '1984' to 'Nineteen Eighty-Four' and save the changes.\n")
file.write(f"Output: {retrieved_book}\n")
