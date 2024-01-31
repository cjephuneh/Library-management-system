from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    membership_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BookDetails(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    number_of_pages = models.PositiveIntegerField()
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.book.title
    
    class Meta:
        verbose_name_plural = "BookDetails"


class BorrowedBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.name + " " + self.book.title
