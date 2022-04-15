from django.contrib import admin
from .models import Movie, Book, Serie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'added', 'modified', 'category', 'rating', 'credits', 'duration')


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('name', 'added', 'modified', 'category', 'rating', 'season', 'episodes')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'added', 'modified', 'category', 'rating', 'pages')
