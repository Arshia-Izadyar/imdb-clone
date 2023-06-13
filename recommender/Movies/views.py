from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .forms import MovieCreateForm, ReviewForm, CommentForm
from .models import MovieModel


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
    

class MovieReview(DetailView):
    model = MovieModel  

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            self.object = self.get_object() 
            review = form.save(commit=False)
            review.user = self.request.user
            review.movie = self.object
            review.save()
            return redirect('movie:detail', pk=self.object.pk)
        return render('movie:list')
               
        
class MovieComment(DetailView):
    model = MovieModel
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            self.object = self.get_object() 
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.movie = self.object
            comment.save()
            return redirect('movie:detail', pk=self.object.pk)
        return redirect("movie:list")
        

class MovieDetailView(DetailView):
    context_object_name = 'movie'
    model = MovieModel
    template_name = 'movie/movie_detail.html'
    
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context["review_form"] = ReviewForm() 
        context["comment_form"] = CommentForm()
            
        data = MovieModel.objects.prefetch_related(
            "movie_comment",'movie').get(pk=self.object.pk) 
            
        comment_list = data.movie_comment.all()
        
        rate = data.movie.aggregate(avg_rating=Avg('rating'))
        
        context['comments'] = comment_list  
        context['rate'] = round(rate['avg_rating'], 1)
        return context
    
        
"""

        for score in scores:
            pass
        
        rate = data.movie.avg # sorry for bad naming movie is the ForeignKey for ReviewModel 
        
        average_rate = ReviewModel.objects.filter(movie_id=self.object.pk).aggregate(avg_rate=Avg('rating'))['avg_rate']

        comments = CommentModel.objects.filter(movie_id=self.object.pk)
    
        data = MovieModel.objects.prefetch_related(
            "movie_comment",
            Prefetch('movie', queryset=ReviewModel.objects.aggregate(avg_rate=Avg('rating', output_field=FloatField())))
                ).get(pk=self.object.pk)
        
        comment_list = data.movie_comment.all()
        context['comments'] = comment_list
        
        # average_rate = ReviewModel.objects.filter(movie_id=self.object.pk).aggregate(avg_rate=Avg('rating'))['avg_rate']
        average_rate = data.movie.all().avg_rate
        
        
        context['rate'] = average_rate
        return context
    


"""