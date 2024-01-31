from rest_framework import generics
from .models import User, Book, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BorrowedBooksSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowedBooksListCreateView(generics.ListCreateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
