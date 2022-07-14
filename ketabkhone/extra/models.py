from django.db import models
from book.models import Book
from accounting.models import CustomUser


class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    vote = models.BooleanField()
    create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.vote)


class Publisher(models.Model):
    name = models.CharField(max_length=20)
    addres = models.TextField()
    def __str__ (self):
      return self.name


class Category(models.Model):
    name = models.CharField(max_length=10)
    def __str__ (self):
      return self.name