from django.db import models
from django.contrib.auth.models import User

from lib.validator import check_rate

class GenreModel(models.Model):
    COMEDY = 1
    DRAMA = 2
    HORROR = 3
    ACTION = 4
    MAGIC = 5
    COMIC = 6
    FANTASY = 7 
    genre_type = (
        (COMEDY, "Comedy"),
        (DRAMA, "Drama"), 
        (HORROR, "Horror"), 
        (ACTION, "Action"),
        (COMIC, "Comic"),
        (MAGIC, "Magic"), 
        (FANTASY, "Fantasy")
    )
    title = models.PositiveSmallIntegerField(choices=genre_type, default=ACTION)

    
    def __str__(self):
        return str(self.get_title_display())


class MovieModel(models.Model):
    title = models.CharField(max_length=40, unique=True)
    genre = models.ForeignKey(GenreModel, related_name='movies', on_delete=models.CASCADE)
    release_year = models.DateField()
    plot = models.TextField()
    director = models.CharField(max_length=40)
    
    def __str__(self):
        return self.title


class ReviewModel(models.Model):
    movie = models.ForeignKey(MovieModel, related_name="movie", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    rating = models.DecimalField(validators=[check_rate], decimal_places=1, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.movie.title)
    
    

class CommentModel(models.Model):
    movie = models.ForeignKey(MovieModel, related_name="movie_comment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_list')
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE, related_name="watch_list")
    
    
    def __str__(self):
        return str(self.user.username) # adding str just to make sure
    
    
