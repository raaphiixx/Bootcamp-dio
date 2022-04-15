from django.shortcuts import render
from .models import Movie, Book, Serie

query_movies = Movie.objects.all()
query_book = Book.objects.all()
query_serie = Serie.objects.all()
union = Movie.objects.all().union(Book.objects.all())

context = {
    'movie': query_movies,
    'book': query_book,
    'serie': query_serie,
    'photo': union,
}


def index(request):
    return render(request, 'index.html', context)


def movies(request):
    return render(request, 'movie.html', context)


def books(request):
    return render(request, 'book.html', context)


def series(request):
    return render(request, 'serie.html', context)

