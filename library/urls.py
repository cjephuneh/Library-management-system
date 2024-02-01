from django.urls import path
from .views import (
    # User views
    CreateUserView,
    ListAllUsersView,
    GetUserByIDView,

    # Book views
    AddNewBookView,
    ListAllBooksView,
    GetBookByIdView,
    AssignUpdateBookDetailsView,

    # Borrowed books views
    BorrowBookView,
    ReturnBookView,
    ListBorrowedBooksView,
)

urlpatterns = [
    # User views
    path('users/create/', CreateUserView.as_view(), name='create-user'),
    path('users/list/', ListAllUsersView.as_view(), name='list-users'),
    path('users/<int:id>/', GetUserByIDView.as_view(), name='get-user-by-id'),

    # Book views
    path('books/add/', AddNewBookView.as_view(), name='add_new_book'),
    path('books/list/', ListAllBooksView.as_view(), name='list_all_books'),
    path('books/<int:id>/', GetBookByIdView.as_view(), name='get_book_by_id'),
    path('books/details/assign/', AssignUpdateBookDetailsView.as_view(),
         name='assign_update_book_details'),

    # Borrowed books views
    path('borrow/', BorrowBookView.as_view(), name='borrow_book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return_book'),
    path('list/borrowed/', ListBorrowedBooksView.as_view(),
         name='list_borrowed_books'),
]
