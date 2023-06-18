from django import forms
from .models import MovieModel, ReviewModel, CommentModel, WatchList


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = ("title", "genre", "release_year", "plot", "director")


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ("rating",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ("comment",)


class WatchListForm(forms.ModelForm):
    class Meta:
        model = WatchList
        exclude = ("movie", "user")
