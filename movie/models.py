from django.db import models
from django.db.models.query import QuerySet
from lib.validator import rate_validator
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import timedelta, datetime




class IsActiveManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()


# profile


# genre
class MovieGenre(models.Model):
    ACTION = 1
    HORROR = 2
    COMEDY = 3
    DRAMA = 4
    SIFI = 5
    
    movie_type = (
        (ACTION , "action"),
        (HORROR , "horror"),
        (SIFI , "si_fi"),
        (DRAMA , "drama"),
        (COMEDY , "comedy"),
    )
    
    genre = models.PositiveSmallIntegerField(default=ACTION, choices=movie_type)
    
    def __str__(self):
        return str(self.get_genre_display())


# movie
class Movie(models.Model):
    title = models.CharField(max_length=35, null=False, blank=False, unique=True)
    genre = models.ForeignKey(MovieGenre, related_name='movie', on_delete=models.PROTECT)
    recommended = models.BooleanField(default=True)
    rate = models.PositiveSmallIntegerField(default=1, validators=[rate_validator])
    description = models.TextField(blank=True, null=True)
    # TODO: add support for comments
    times_rated = models.PositiveIntegerField(default=1)
    imdb_rate = models.FloatField(default=1.0, validators=[rate_validator])
    release_date = models.DateField(null=True, blank=True)
    user_creator = models.ForeignKey(User, related_name='movie_user', on_delete=models.PROTECT, null=True)
    modified_date = models.DateField(auto_now=True)
    next_allowed_modify = models.DateTimeField(
            default=datetime.now()+timedelta(minutes=10)-timedelta(hours=5) # adjust for UTC
        )

    objects = IsActiveManager()
    default_manager = models.Manager()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("movie-show", kwargs={"pk": self.pk})
    

 