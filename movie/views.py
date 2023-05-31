from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from movie.forms import MovieForm
from movie.models import Movie
from django.views.generic import ListView, DetailView,UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core import exceptions
from datetime import datetime, timedelta
from movie.filter import MovieFilter


class MovieListView(ListView):
    context_object_name = "movie_list"
    queryset = Movie.objects.all()
    template_name = "movie/movie_list.html"
    
    def get_queryset(self) :
        query_set =  super().get_queryset()
        self.filterset = MovieFilter(self.request.GET, queryset=query_set)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class MovieCreateView(FormView):
    form_class = MovieForm
    template_name = "movie/movie_create.html"
    success_url = reverse_lazy('movie_list')
    
    # def get_success_url(self):
    #     return reverse("movie-show", kwargs={"pk": self.pk})
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user_creator = self.request.user
        instance.save()
        return super().form_valid(form)
    


class MovieDetailView(UpdateView):
    template_name = "movie/movie_detail.html"
    context_object_name = "movie_detail"
    model = Movie
    # form_class = MovieUpdateForm
    fields = ('rate',)
    template_name_suffix = "_update_form"
    
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):

    #     access_time = request.session['last_access'] = datetime.today().strftime('%Y-%m-%d')
    #     next_access_time = request.session['next_access'] = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    #     print(next_access_time )
    #     # if access_time < next_access_time:
    #     self.object = self.get_object()
    #     print(self.object.rate)
    #     print(self.object.total_rate)
    #     print(self.object.get_rate(self.object.rate))
    #     self.object.get_rate(self.object.rate)
    #     self.object.save()
    #     # else:
    #     #     return HttpResponseRedirect('/movie/too-many-attempts/')

    #     return HttpResponseRedirect('/movie/list/')


    def post(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        self.object.save()
        self.form = self.get_form()
        self.form.save(commit=False)
        self.object.rate = self.object.get_rate(self.object.rate)
        self.form.save()


        
        
        
        return HttpResponseRedirect('/movie/list/')