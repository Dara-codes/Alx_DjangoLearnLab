# from django.test import TestCase
# from django.contrib.auth.models import User
# from rest_framework.test import APIClient
# from rest_framework import status
# from model_bakery import baker

# from .models import Book
# from .serializers import BookSerializer

# class BookAPITestCase(TestCase):
#     def setUp(self):
#         """
#         Set up test environment before each test method.
#         - Create test client
#         - Create test users
#         - Create sample books
#         """
#         self.client = APIClient()
        
#         # Create test users
#         self.admin_user = User.objects.create_superuser(
#             username='admin', 
#             email='admin@example.com', 
#             password='adminpass123'
#         )
#         self.regular_user = User.objects.create_user(
#             username='user', 
#             email='user@example.com', 
#             password='userpass123'
#         )
        
#         # Create sample books using model_bakery
#         self.books = baker.make(
#             'books.Book', 
#             _quantity=10,
#             title=baker.sequence(lambda c: f'Book {c}'),
#             author=baker.sequence(lambda c: f'Author {c}')
#         )

#     def test_book_list_view(self):
#         """
#         Test retrieving the list of books
#         - Verify correct number of books returned
#         - Check response status code
#         """
#         response = self.client.get('/api/books/')
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data['results']), 10)

#     def test_book_create_authenticated(self):
#         """
#         Test book creation with authenticated user
#         - Verify successful book creation
#         - Check response status and data
#         """
#         # Log in as admin
#         self.client.force_authenticate(user=self.admin_user)
        
#         book_data = {
#             'title': 'New Test Book',
#             'author': 'Test Author',
#             'publication_year': 2023,
#             'genre': 'Fiction'
#         }
        
#         response = self.client.post('/api/books/', book_data)
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['title'], book_data['title'])
#         self.assertEqual(Book.objects.count(), 11)

#     def test_book_create_unauthenticated(self):
#         """
#         Test book creation without authentication
#         - Verify unauthorized access is prevented
#         """
#         book_data = {
#             'title': 'Unauthorized Book',
#             'author': 'Unauthorized Author',
#         }
        
#         response = self.client.post('/api/books/', book_data)
        
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_book_update(self):
#         """
#         Test updating an existing book
#         - Verify successful update
#         - Check updated data matches
#         """
#         self.client.force_authenticate(user=self.admin_user)
        
#         book = self.books[0]
#         update_data = {
#             'title': 'Updated Book Title',
#             'author': book.author
#         }
        
#         response = self.client.patch(f'/api/books/{book.id}/', update_data)
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], 'Updated Book Title')

#     def test_book_delete(self):
#         """
#         Test deleting a book
#         - Verify book is removed
#         - Check response status
#         """
#         self.client.force_authenticate(user=self.admin_user)
        
#         book = self.books[0]
#         response = self.client.delete(f'/api/books/{book.id}/')
        
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Book.objects.filter(id=book.id).exists())

#     def test_book_filtering(self):
#         """
#         Test filtering books
#         - Verify filtering by author works correctly
#         """
#         # Create some specific books for filtering
#         baker.make('books.Book', author='J.R.R. Tolkien', _quantity=3)
#         baker.make('books.Book', author='George R.R. Martin', _quantity=2)
        
#         response = self.client.get('/api/books/?author=Tolkien')
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data['results']), 3)

#     def test_book_search(self):
#         """
#         Test search functionality
#         - Verify searching by title works
#         """
#         # Create books with specific titles
#         baker.make('books.Book', title='Fantasy Epic', _quantity=2)
#         baker.make('books.Book', title='Sci-Fi Adventure', _quantity=1)
        
#         response = self.client.get('/api/books/?search=Fantasy')
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data['results']), 2)

#     def test_book_ordering(self):
#         """
#         Test ordering functionality
#         - Verify books can be ordered by title
#         """
#         # Create books with specific titles for ordering test
#         baker.make('books.Book', title='A First Book', publication_year=2000)
#         baker.make('books.Book', title='Z Last Book', publication_year=2010)
        
#         # Test ascending order
#         response = self.client.get('/api/books/?ordering=title')
#         titles = [book['title'] for book in response.data['results']]
#         self.assertTrue(titles == sorted(titles))
        
#         # Test descending order
#         response = self.client.get('/api/books/?ordering=-title')
#         titles = [book['title'] for book in response.data['results']]
#         self.assertTrue(titles == sorted(titles, reverse=True))

#     def test_book_year_range_filter(self):
#         """
#         Test filtering books by publication year range
#         """
#         # Create books with specific publication years
#         baker.make('books.Book', publication_year=1990, _quantity=2)
#         baker.make('books.Book', publication_year=2010, _quantity=3)
#         baker.make('books.Book', publication_year=2020, _quantity=1)
        
#         response = self.client.get('/api/books/?min_publication_year=2000&max_publication_year=2015')
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data['results']), 3)


from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from model_bakery import baker

from .models import Book
from .serializers import BookSerializer

class BookAPITestCase(TestCase):
    def setUp(self):
        """
        Set up test environment before each test method.
        - Create test client
        - Create test users
        - Create sample books
        """
        self.client = APIClient()
        
        # Create test users
        self.admin_user = User.objects.create_superuser(
            username='admin', 
            email='admin@example.com', 
            password='adminpass123'
        )
        self.regular_user = User.objects.create_user(
            username='user', 
            email='user@example.com', 
            password='userpass123'
        )
        
        # Create sample books using model_bakery
        self.books = baker.make(
            'Book', 
            _quantity=10,
            title=baker.sequence(lambda c: f'Book {c}'),
            author=baker.sequence(lambda c: f'Author {c}')
        )

    def test_book_list_view(self):
        """
        Test retrieving the list of books
        - Verify correct number of books returned
        - Check response status code
        """
        response = self.client.get('/api/books/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_book_create_authenticated(self):
        """
        Test book creation with authenticated user
        - Verify successful book creation
        - Check response status and data
        """
        self.client.login(username='admin', password='adminpass123')
        
        book_data = {
            'title': 'New Test Book',
            'author': 'Test Author',
            'publication_year': 2023,
            'genre': 'Fiction'
        }
        
        response = self.client.post('/api/books/', book_data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], book_data['title'])
        self.assertEqual(Book.objects.count(), 11)
        self.client.logout()

    def test_book_create_unauthenticated(self):
        """
        Test book creation without authentication
        - Verify unauthorized access is prevented
        """
        book_data = {
            'title': 'Unauthorized Book',
            'author': 'Unauthorized Author',
        }
        
        response = self.client.post('/api/books/', book_data)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_book_update(self):
        """
        Test updating an existing book
        - Verify successful update
        - Check updated data matches
        """
        self.client.login(username='admin', password='adminpass123')
        
        book = self.books[0]
        update_data = {
            'title': 'Updated Book Title',
            'author': book.author
        }
        
        response = self.client.patch(f'/api/books/{book.id}/', update_data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book Title')
        self.client.logout()

    def test_book_delete(self):
        """
        Test deleting a book
        - Verify book is removed
        - Check response status
        """
        self.client.login(username='admin', password='adminpass123')
        
        book = self.books[0]
        response = self.client.delete(f'/api/books/{book.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book.id).exists())
        self.client.logout()

    def test_book_filtering(self):
        """
        Test filtering books
        - Verify filtering by author works correctly
        """
        # Create some specific books for filtering
        baker.make('Book', author='J.R.R. Tolkien', _quantity=3)
        baker.make('Book', author='George R.R. Martin', _quantity=2)
        
        response = self.client.get('/api/books/?author=Tolkien')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_book_search(self):
        """
        Test search functionality
        - Verify searching by title works
        """
        # Create books with specific titles
        baker.make('Book', title='Fantasy Epic', _quantity=2)
        baker.make('Book', title='Sci-Fi Adventure', _quantity=1)
        
        response = self.client.get('/api/books/?search=Fantasy')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_ordering(self):
        """
        Test ordering functionality
        - Verify books can be ordered by title
        """
        # Create books with specific titles for ordering test
        baker.make('Book', title='A First Book', publication_year=2000)
        baker.make('Book', title='Z Last Book', publication_year=2010)
        
        # Test ascending order
        response = self.client.get('/api/books/?ordering=title')
        titles = [book['title'] for book in response.data]
        self.assertTrue(titles == sorted(titles))
        
        # Test descending order
        response = self.client.get('/api/books/?ordering=-title')
        titles = [book['title'] for book in response.data]
        self.assertTrue(titles == sorted(titles, reverse=True))

    def test_book_year_range_filter(self):
        """
        Test filtering books by publication year range
        """
        # Create books with specific publication years
        baker.make('Book', publication_year=1990, _quantity=2)
        baker.make('Book', publication_year=2010, _quantity=3)
        baker.make('Book', publication_year=2020, _quantity=1)
        
        response = self.client.get('/api/books/?min_publication_year=2000&max_publication_year=2015')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
