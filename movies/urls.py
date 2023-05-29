from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.MoviesView.as_view(), name='movies')
]
