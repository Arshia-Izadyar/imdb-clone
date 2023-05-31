from django.urls import path
from django.views.generic import TemplateView

from movie.views import MovieListView, MovieCreateView, MovieDetailView


urlpatterns = [
    # genre list
    
    # movie list
    path('list/', MovieListView.as_view(), name='movie_list'),
    path('create/', MovieCreateView.as_view(), name='movie-create'),
    path('too-many-attempts/' ,TemplateView.as_view(template_name="movie/too_many_attempts.html")),
    # selected movie
    path('show/<int:pk>/',MovieDetailView.as_view(), name='movie-show'),
    # User profile 
    
    # login
    
    # logout
    
    # sign in
    
]
