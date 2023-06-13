from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView


from Movies.models import MovieModel, ReviewModel
from .serializer import MovieListSerializer, MovieDetailSerializer, ReviewSerializer


class MovieListApiView(ListAPIView):
    serializer_class = MovieListSerializer
    model = MovieModel
    queryset = MovieModel.objects.all()


class MovieDetailApiView(RetrieveUpdateAPIView):
    serializer_class = MovieDetailSerializer
    model = MovieModel
    queryset = MovieModel.objects.prefetch_related('movie', 'movie_comment')
    
    
class ReviewCreateApiView(CreateAPIView):
    model = ReviewModel
    serializer_class = ReviewSerializer