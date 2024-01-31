from django.urls import path
from .views import UserListCreateView, BookListCreateView, BorrowedBooksListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('borrowed-books/', BorrowedBooksListCreateView.as_view(), name='borrowed-books-list-create'),
]