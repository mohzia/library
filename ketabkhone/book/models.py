from django.db import models
from accounting.models import User


class Book (models.Model):
    name = models.CharField(max_length=30)
    cover = models.ImageField(
        upload_to='media', default='Default.jpg')
    create = models.DateTimeField(auto_now_add=True)
    modifield = models.DateTimeField(auto_now=True)
    desk = models.TextField()
    translator = models.CharField(max_length=30)
    # related_name reverse_relation
    poblisher = models.ForeignKey(
        "extra.Publisher", on_delete=models.DO_NOTHING)
    category = models.ManyToManyField("extra.Category")
    author = models.ManyToManyField("author.Author")
    user = models.ForeignKey("accounting.CustomUser", on_delete=models.CASCADE)
    active = models.BooleanField()
    loan = models.ForeignKey("loan.Loan", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.ManyToManyField("book.Book")
    create = models.DateTimeField(auto_now_add=True)
    modifiled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
