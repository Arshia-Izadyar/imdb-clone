from django.db import models
from django.contrib.auth.models import User

class GenreModel(models.Model):
    title = models.CharField(max_length=35)



class MovieModel(models.Model):
    title = models.CharField(max_length=40)
    genre = models.ForeignKey(GenreModel, related_name='movies', on_delete=models.CASCADE)
    release_year = models.DateField()
    plot = models.TextField()
    director = models.CharField(max_length=40)
    
    def __str__(self):
        return self.title


class ReviewModel(models.Model):
    movie = models.ForeignKey(MovieModel, related_name="movie", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.movie.title)
    
    
class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_list')
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE, related_name="watch_list")
    
    
    def __str__(self):
        return str(self.user.username) # adding str just to make sure
    
    
