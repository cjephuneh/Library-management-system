from django.contrib import admin

# Register your models here.
from .models import Book, BookDetails, BorrowedBooks, User

admin.site.register(Book)
admin.site.register(BookDetails)
admin.site.register(BorrowedBooks)
admin.site.register(User)