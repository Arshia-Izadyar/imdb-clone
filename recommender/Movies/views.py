from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

from .forms import MovieCreateForm, ReviewForm
from .models import MovieModel, ReviewModel


class MovieListView(ListView):
    model = MovieModel
    queryset = MovieModel.objects.all()
    template_name = "movie/movie_list.html"
    context_object_name = "movies"
    
    
class MovieCreateView(FormView):
    success_url = reverse_lazy('movie:list')
    template_name = 'movie/movie_create.html'
    form_class = MovieCreateForm
    
    
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class MovieReview(View): 
    
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        
        return super().dispatch(request, *args, **kwargs)
    
from django.views.generic import DetailView

class MovieReview(DetailView):
    model = MovieModel  

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = self.request.user
            review.movie = self.get_object() 
            review.save()
            return redirect('movie:list')

  
    
class MovieDetailView(DetailView):
    context_object_name = 'movie'
    model = MovieModel
    template_name = 'movie/movie_detail.html'
    
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review_form"] = ReviewForm() 
        context['review'] = ReviewModel.objects.filter(movie=self.object)
        return context
    