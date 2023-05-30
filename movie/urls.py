from django.urls import path
from movie.views import MovieListView, MovieCreateView, MovieDetailView


urlpatterns = [
    # User profile 
    # genre list
    # movie list
    path('list/', MovieListView.as_view(), name='movie_list'),
    path('create/', MovieCreateView.as_view(), name='movie-create'),
    path('show/<int:pk>/',MovieDetailView.as_view(), name='movie-show'),
    # selected movie
    
]
