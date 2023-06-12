from django.urls import path
from .views import MovieListView, MovieCreateView, MovieDetailView, MovieReview

app_name = 'movie'

urlpatterns = [
    path('list/', MovieListView.as_view(), name="list"),
    path('create/', MovieCreateView.as_view(), name="create"),
    path('detail/<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path("detail/<int:pk>/create_review/", MovieReview.as_view(), name="create_review"),
]
