from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy

from .forms import MovieCreateForm
from .models import MovieModel


class MovieListView(ListView):
    model = MovieModel
    queryset = MovieModel.objects.all()
    template_name = "movie/movie_list.html"
    context_object_name = "movies"
    
    
class MovieCreateView(FormView):
    success_url = reverse_lazy('movie-list')
    template_name = 'movie/movie_create.html'
    form_class = MovieCreateForm
    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    