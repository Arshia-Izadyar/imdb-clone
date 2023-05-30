from django.http import HttpResponse
from django.shortcuts import render
from movie.forms import MovieForm
from movie.models import Movie
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class MovieListView(ListView):
     context_object_name = "movie_list"
     queryset = Movie.objects.all()
     template_name = "movie/movie_list.html"
    #  form_class = MovieForm
    
    
class MovieCreateView(FormView):
    form_class = MovieForm
    template_name = "movie/movie_create.html"
    success_url = reverse_lazy('movie_list')
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_creator = self.request.user
        instance.save()
        return super().form_valid(form)