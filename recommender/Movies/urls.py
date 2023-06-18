from django.urls import path
from .views import MovieListView, MovieCreateView, MovieDetailView, MovieReview, MovieComment, MovieWatchList

app_name = "movie"

urlpatterns = [
    path("list-movie/", MovieListView.as_view(), name="list"),
    path("create-movie/", MovieCreateView.as_view(), name="create"),
    path("detail-movie/<int:pk>/", MovieDetailView.as_view(), name="detail"),
    path("detail/<int:pk>/create_review/", MovieReview.as_view(), name="create_review"),
    path("detail/<int:pk>/create_comment/", MovieComment.as_view(), name="create_comment"),
    path("detail/<int:pk>/create_watchlist/", MovieWatchList.as_view(), name="create_watchlist"),
]
