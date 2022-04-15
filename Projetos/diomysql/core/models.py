from django.db import models

# Create your models here.
from django.db import models
from stdimage import StdImageField
from django.template.defaultfilters import slugify
from django.db.models import signals


class Base(models.Model):
    name = models.CharField('Nome', max_length=60)
    description = models.TextField('Resumo', max_length=300)
    added = models.DateField('Criado em', auto_now_add=True)
    modified = models.DateField('Modificado em', auto_now=True)
    CATEGORY_CHOICES = (
        ('Ação', 'Ação'),
        ('Animação', 'Animação'),
        ('Aventura', 'Aventura'),
        ('Comédia', 'Comédia'),
        ('Documentário', 'Documentário'),
        ('Drama', 'Drama'),
        ('Ficção Cientifica', 'Ficção Cientifica'),
        ('Musical', 'Musical'),
        ('Romance', 'Romance'),
        ('Suspense', 'Suspense'),
        ('Terror', 'Terror'),
    )
    category = models.CharField('Categoria', max_length=100, choices=CATEGORY_CHOICES, default=None)
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rating = models.SmallIntegerField('Nota', choices=RATING_CHOICES, default=None)

    class Meta:
        abstract = True


class Movie(Base):
    poster = StdImageField('Poster', upload_to='pictures')
    credits = models.BooleanField('Pós-Crédito', default=False)
    duration = models.DurationField('Duration')
    slug = models.SlugField('Slug', max_length=50, blank=True, editable=False)


class Book(Base):
    poster = StdImageField('Poster', upload_to='pictures')
    author = models.CharField('Autor', max_length=50, blank=True)
    pages = models.PositiveSmallIntegerField('Total de Páginas')
    slug = models.SlugField('Slug', max_length=50, blank=True, editable=False)


class Serie(Base):
    poster = StdImageField('Poster', upload_to='pictures')
    season = models.PositiveSmallIntegerField('Quantidade de Temporadas')
    episodes = models.PositiveSmallIntegerField('Episódios por Temporada')
    slug = models.SlugField('Slug', max_length=50, blank=True, editable=False)


def movie_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


def book_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


def serie_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(movie_pre_save, sender=Movie)
signals.pre_save.connect(book_pre_save, sender=Book)
signals.pre_save.connect(serie_pre_save, sender=Serie)
