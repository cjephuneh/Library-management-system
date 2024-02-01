from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from library.models import User, Book, BorrowedBooks


class BorrowedBooksAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_borrow_book(self):
        user = User.objects.create(
            name='Test User', email='test@example.com', membership_date='2022-01-01')
        book = Book.objects.create(
            title='Test Book', isbn='1234567890123', published_date='2022-01-01', genre='Fiction')
        url = reverse('borrow_book')
        data = {'user': user.id, 'book': book.id, 'borrow_date': '2022-02-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_return_book(self):
        user = User.objects.create(
            name='Test User', email='test@example.com', membership_date='2022-01-01')
        book = Book.objects.create(
            title='Test Book', isbn='1234567890123', published_date='2022-01-01', genre='Fiction')

        # Borrow the book
        url_borrow = reverse('borrow_book')
        borrow_data = {'user': user.id, 'book': book.id, 'borrow_date': '2022-02-01'}
        response = self.client.post(url_borrow, borrow_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get the BorrowedBooks object
        borrowed_book = BorrowedBooks.objects.get(user=user, book=book)

        # Return the book
        url_return = reverse('return_book', args=[borrowed_book.id])
        borrow_data['return_date'] = '2022-02-15'
        response = self.client.put(url_return, borrow_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_list_borrowed_books(self):
        url = reverse('list_borrowed_books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
