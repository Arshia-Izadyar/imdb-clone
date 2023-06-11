from django import forms
from .models import MovieModel



class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = ('title', 'genre', 'release_year', 'plot', 'director')