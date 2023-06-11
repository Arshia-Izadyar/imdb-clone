from django.contrib import admin
from django.contrib.admin import register, ModelAdmin
from .models import MovieModel, GenreModel


@register(MovieModel)
class MovieAdmin(ModelAdmin):
    list_display = ("title", 'genre', 'release_year')
    list_filter =  ('genre',)
    
    
@register(GenreModel)
class GenreAdmin(ModelAdmin):
    list_display = ('title',)