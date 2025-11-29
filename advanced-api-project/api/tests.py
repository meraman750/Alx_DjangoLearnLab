from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """Test suite for Book API endpoints including CRUD, filtering, searching, ordering, and permissions."""

    def setUp(self):
        # Set up test user and authentication
        self.user = User.objects.create_user(username="tester", password="pass1234")
        self.client = APIClient()

        # Create sample author and books
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author
        )

    # ---------------------------
    # CRUD TESTS
    # ---------------------------

    def test_get_book_list(self):
        """Ensure GET /books/ returns book list successfully."""
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_requires_authentication(self):
        """Ensure unauthenticated user cannot create a book."""
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Ensure authenticated user can create a book."""
        self.client.login(username="tester", password="pass1234")
        data = {
            "title": "Fantastic Beasts",
            "publication_year": 2016,
            "author": self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """Ensure authenticated user can update a book."""
        self.client.login(username="tester", password="pass1234")
        response = self.client.put(
            reverse('book-update', args=[self.book1.id]),
            {"title": "Updated Title", "publication_year": 1997, "author": self.author.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Ensure authenticated user can delete a book."""
        self.client.login(username="tester", password="pass1234")
        response = self.client.delete(reverse('book-delete', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------------------------
    # FILTER, SEARCH, ORDER TESTS
    # ---------------------------

    def test_filter_books_by_year(self):
        """Test filtering with ?publication_year=1998"""
        response = self.client.get('/api/books/?publication_year=1998')
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching titles with ?search=Chamber"""
        response = self.client.get('/api/books/?search=Chamber')
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year_desc(self):
        """Test ordering with ?ordering=-publication_year"""
        response = self.client.get('/api/books/?ordering=-publication_year')
        self.assertEqual(response.data[0]['publication_year'], 1998)
