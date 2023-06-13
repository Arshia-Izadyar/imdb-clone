from rest_framework.urls import path

from .views import MovieListApiView, MovieDetailApiView, ReviewCreateApiView

app_name = "api"

urlpatterns = [
    path('movie-list/', MovieListApiView.as_view(), name="movie-list"),
    path('movie-detail/<int:pk>/', MovieDetailApiView.as_view(), name="movie-detail"),
    path('movie-Review/', ReviewCreateApiView.as_view(), name="movie-review"),
    
    
]
