from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from library.models import Book, BookDetails


class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_add_new_book(self):
        url = reverse('add_new_book')
        data = {'title': 'Test Book', 'isbn': '1234567890123',
                'published_date': '2022-01-01', 'genre': 'Fiction'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all_books(self):
        url = reverse('list_all_books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_by_id(self):
        book = Book.objects.create(
            title='Test Book', isbn='1234567890123', published_date='2022-01-01', genre='Fiction')
        url = reverse('get_book_by_id', args=[book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_assign_update_book_details(self):
        book = Book.objects.create(
            title='Test Book', isbn='1234567890123', published_date='2022-01-01', genre='Fiction')
        url = reverse('assign_update_book_details')
        data = {'book': book.id, 'number_of_pages': 200,
                'publisher': 'Test Publisher', 'language': 'English'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
