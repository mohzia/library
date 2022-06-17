from django.shortcuts import render
from book.models import Book

def bookdetail(request):
    return render(request, 'bookdetail.html',)

def bookliste(request):
    return render(request, 'bookliste.html')

def btest(request):
    return render(request, 'btest.html')


def contest(request):
    context = {'book': Book.objects.all() , 'imgs':Book.objects.cover()}
    return render(request, 'contest.html',context)
