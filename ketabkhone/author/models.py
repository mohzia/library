from unicodedata import name
from django.db import models
from django.forms import CharField


class Author(models.Model):
    def __str__ (self):
      return self.name
    name = models.CharField(max_length=15)
    description = models.TextField()
