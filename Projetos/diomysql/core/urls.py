from django.urls import path
from .views import index, movies, books, series
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('movies/', movies, name='movies'),
    path('books/', books, name='books'),
    path('series/', series, name='series'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
