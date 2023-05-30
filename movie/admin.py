from django.contrib.admin import ModelAdmin, register, TabularInline
from movie.models import Movie, MovieGenre

class MovieTabularInline(TabularInline): 
    model = Movie




@register(Movie)
class MovieAdmin(ModelAdmin):
    list_display = ('title', 'rate', 'times_rated','genre')
    list_filter = ('genre',)
    search_fields = ('title',)
    # inlines = [MovieTabularInline]
    
@register(MovieGenre)
class GenreAdmin(ModelAdmin):
    list_display = ('genre', )