from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import MovieModel


class MovieList(ListView):
    model = MovieModel
    queryset = MovieModel.objects.all()
    template_name = "movie/movie_list.html"
    context_object_name = "movies"
    