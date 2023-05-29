from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MoviePost(models.Model):
    user = models.ForeignKey(User, related_name='movie_posts', on_delete=models.PROTECT)
    title = models.CharField(max_length=35)
    rate = models.PositiveSmallIntegerField(null=True, blank=True, default=1)
    comment = models.TextField(blank=True, null=True)
    # TODO: Add support for comments
    times_watched = models.PositiveIntegerField(null=True, blank=True, default=1)
    watch_list = models.BooleanField(null=True, blank=True, default=False) 
    recommended = models.BooleanField(null=True, blank=True, default=True)
    time = models.DateTimeField(auto_now_add=True)
    