```python
>>>from bookshelf.models import Book
Book.objects.get(title="1984")
>>> book1.title 
#output
retrieved_book = Book.objects.filter(title="1984").first()
print(retrieved_book)


