from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from movie.forms import MovieForm
from movie.models import Movie
from django.views.generic import ListView, DetailView,UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core import exceptions
from datetime import datetime, date
# from django.urls import reverse

class MovieListView(ListView):
     context_object_name = "movie_list"
     queryset = Movie.objects.all()
     template_name = "movie/movie_list.html"
    
    
class MovieCreateView(FormView):
    form_class = MovieForm
    template_name = "movie/movie_create.html"
    success_url = reverse_lazy('movie_list')
    
    # def get_success_url(self):
    #     return reverse("movie-show", kwargs={"pk": self.pk})
    
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_creator = self.request.user
        instance.save()
        return super().form_valid(form)
    


class MovieDetailView(UpdateView):
    template_name = "movie/movie_detail.html"
    context_object_name = "movie_detail"
    model = Movie
    fields = ("rate",)
    template_name_suffix = "_update_form"
    
    # def get(self, request, pk, *args, **kwargs):
    #     object = self.queryset.get(pk=pk)
    #     return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        # instance = form.save(commit=False)
        # instance.user_creator = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        # if self.object.modified_date < date.today():
        form = self.get_form()
        self.object.times_rated += 10
        form.save()
        
        # self.object.times_rated.save()
        # else:
        #     form = self.get_form()
        #     form.save(commit=False)
        #     raise exceptions.TooManyFieldsSent("lol")
       
        
        return super().post(request, *args, **kwargs)
