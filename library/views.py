from .models import (
    User,
    Book,
    BookDetails,
    BorrowedBooks
)
from .serializers import (
    UserSerializer,
    BookSerializer,
    BookDetailsSerializer,
    BorrowedBooksSerializer
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView
)


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListAllUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserByIDView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

# Book views


class AddNewBookView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListAllBooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GetBookByIdView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class AssignUpdateBookDetailsView(CreateAPIView):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer


# Borrowed books views
class BorrowBookView(CreateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer


class ReturnBookView(UpdateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer


class ListBorrowedBooksView(ListAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
