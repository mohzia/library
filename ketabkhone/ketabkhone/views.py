from django.contrib.auth import authenticate
from enum import auto
from unicodedata import category
from urllib import request
from django.shortcuts import render, redirect
from book.models import Book, Bookmark , Comment
from extra.models import Category, Like
from accounting.models import CustomUser
from .forms import Search
from django.db.models import Q
from django.contrib.auth import authenticate

def bookdetail(request, book_id):
    book_obj = Book.objects.get(id=book_id)
    likes = Like.objects.filter(book_id=book_id, vote=True).count()
    comments = Comment.objects.filter(book=book_obj)
    dislikes = Like.objects.filter(book_id=book_id, vote=False).count()
    return render(request, 'bookdetail.html', {'book_obj': book_obj, 'likes': likes, "dislike": dislikes, "comments":comments})


def bookliste(request):
    form = Search()
    # print(request.GET)
    if "search_form" in request.GET:
        # print(request.GET.get('search_form'))
        form_em = Search(request.GET)
        if form_em.is_valid():
            search_text = form_em.cleaned_data['search_form']
            context = {
                'book': Book.objects.filter(Q(name__icontains=search_text) | Q(category__name__icontains=search_text) | Q(author__name__icontains=search_text) ),
                "form": form,
            }
    else:
        context = {
            'book': Book.objects.all(),
            "form": form,
        }
    return render(request, 'bookliste.html', context)


def btest(request):
    return render(request, 'btest.html')


def contest(request):
    context = {'book': Book.objects.all()}
    return render(request, 'contest.html', context)


def category_bookliste(request, category_id):
    context = {'book': Book.objects.filter(category=category_id)}
    return render(request, "bookliste.html", context)


def like(request, book_id):
    customuser = CustomUser.objects.get(user=request.user)
    book = Book.objects.get(id=book_id)
    if Like.objects.filter(user=customuser, book=book).exists():
        if not Like.objects.filter(user=customuser, book=book, vote=True).exists():
            like = Like.objects.get(user=customuser, book=book)
            like.vote = True
            like.save()
    else:
        Like.objects.create(user=customuser, book=book, vote=True)
    return redirect("bookdetail_page", book_id=book_id)


def dislike(request, book_id):
    customuser = CustomUser.objects.get(user=request.user)
    book = Book.objects.get(id=book_id)
    if Like.objects.filter(user=customuser, book=book).exists():
        if not Like.objects.filter(user=customuser, book=book, vote=False).exists():
            like = Like.objects.get(user=customuser, book=book)
            like.vote = False
            like.save()
    else:
        Like.objects.create(user=customuser, book=book, vote=False)
    return redirect("bookdetail_page", book_id=book_id)


def author_list(request, auth_id):
    context = {'book': Book.objects.filter(author=auth_id)}
    return render(request, "bookliste.html", context)


def bookmark(request, book_id):
    book = Book.objects.get(id=book_id)
    if Bookmark.objects.filter(user=request.user).exists():
        if Bookmark.objects.filter(user=request.user, book=book).exists():
            bookmarkbooks = Bookmark.objects.get(user=request.user)
            bookmarkbooks.book.remove(book)
            bookmarkbooks.save()
        else:
            bookmarkbooks = Bookmark.objects.get(user=request.user)
            bookmarkbooks.book.add(book)
            bookmarkbooks.save()
    else:
        bookmark_obj = Bookmark.objects.create(user=request.user)
        bookmark_obj.book.add(book)
        bookmark_obj.save()
    return redirect("bookdetail_page", book_id=book_id)

def nbooklist(request):
    return render(request,"newbookliste.html")

def login(request):
    if request.method=="POST":
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        details = username,password
        usernames = CustomUser.objects.all()
        user = details.authenticate(username in username, password in password)
        if user.is_authenticated:
            print("hi")
    # authenticate
    # login
    # session va cookie 
    return render(request, "login.html")

def add_comment(request, book_id):
    add_commit = request.POST['add_commit']
    add_title = request.POST['add_title']
    print(add_title , add_comment)
    return redirect("bookdetail_page", book_id=book_id)
