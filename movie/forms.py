from django import forms
from movie.models import Movie
from lib.validator import rate_validator

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'genre', 'recommended', 'rate', 'description', 'imdb_rate', 'release_date')
        
        
# class MovieUpdateForm(forms.ModelForm):
#     rate = forms.FloatField(validators=[rate_validator])
#     class Meta:
#         model = Movie
#         fields = ('rate',)
        