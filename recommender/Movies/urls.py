from django.urls import path
from .views import MovieListView, MovieCreateView

urlpatterns = [
    path('list/', MovieListView.as_view(), name="movie-list"),
    path('create/', MovieCreateView.as_view(), name="movie-create"),
]
