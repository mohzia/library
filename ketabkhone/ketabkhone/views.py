from django.shortcuts import render , redirect
from book.models import Book
from extra.models import Like
from accounting.models import CustomUser

def bookdetail(request, book_id ):
    book_obj = Book.objects.get(id=book_id)
    likes = Like.objects.filter(book_id=book_id , vote=True).count()
    dislikes = Like.objects.filter(book_id=book_id , vote=False).count()
    return render(request, 'bookdetail.html', {'book_obj': book_obj , 'likes':likes , "dislike":dislikes})

def bookliste(request):
    context = {'book': Book.objects.all() }
    return render(request, 'bookliste.html',context)

def btest(request):
    return render(request, 'btest.html')


def contest(request):
    context = {'book': Book.objects.all() }
    return render(request, 'contest.html',context)

def category_bookliste(request , category_id):
    context = {'book': Book.objects.filter(category=category_id) }
    return render(request,"bookliste.html",context)

def like (request , book_id):
    customuser = CustomUser.objects.get(user=request.user)
    book=Book.objects.get(id=book_id)
    if Like.objects.filter(user=customuser , book=book).exists():
        if not Like.objects.filter(user=customuser , book=book , vote=True).exists():
            like=Like.objects.get(user=customuser,book=book)
            like.vote=True
            like.save()
    else:
        Like.objects.create(user=customuser , book=book , vote=True)
    return redirect ("bookdetail_page" , book_id = book_id)

def dislike (request , book_id):
    customuser = CustomUser.objects.get(user=request.user)
    book=Book.objects.get(id=book_id)
    if Like.objects.filter(user=customuser , book=book).exists():
        if not Like.objects.filter(user=customuser , book=book , vote=False).exists():
            like=Like.objects.get(user=customuser,book=book)
            like.vote=False
            like.save()
    else:
        Like.objects.create(user=customuser , book=book , vote=False)
    return redirect ("bookdetail_page" , book_id = book_id)

def author_list (request , auth_id):
    context={'book':Book.objects.filter(author=auth_id)}
    return render(request,"bookliste.html",context)