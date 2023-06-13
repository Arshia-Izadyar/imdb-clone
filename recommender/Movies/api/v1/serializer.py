from rest_framework import serializers
from django.db.models import Avg

from Movies.models import MovieModel, ReviewModel


class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieModel
        fields = ('title', 'genre', 'release_year', 'plot', 'director')
        

        
class MovieDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    
    def get_rate(self, obj):
        rate = obj.movie.aggregate(avg_rating=Avg('rating'))
        return round(rate['avg_rating'], 1)
    
    def get_comments(self, obj):
        comments = obj.movie_comment.all()
        return [comment.comment for comment in comments]
            
    
    class Meta:
        model = MovieModel
        fields = ('title', 'genre', 'release_year', 'plot', 'director', 'rate', 'comments')
        read_only_fields = ('title', 'genre', 'release_year', 'plot', 'director', 'rate', 'comments')
        
        
        
        
class ReviewSerializer(serializers.ModelSerializer):
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        movie_serializer = MovieListSerializer(instance)
        representation.update(movie_serializer.data)
        return representation

    class Meta:
        model = ReviewModel
        fields = ('movie', 'user', 'rating')
        
        
    