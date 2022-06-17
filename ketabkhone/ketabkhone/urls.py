from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import bookdetail
from ketabkhone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookdetail/', views.bookdetail , name="bookdetail page"),
    path('bookliste/', views.bookliste , name="booklist page"),
    path('contest/', views.contest , name="contest page"),
    path('btest/', views.btest , name="btest page"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
