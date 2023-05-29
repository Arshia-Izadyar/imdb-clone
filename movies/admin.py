from django.contrib import admin
from django.contrib.admin import register
from movies.models import MoviePost

@register(MoviePost)
class MoviePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'time')
    search_fields = ('rate', 'user__username', 'title')
    list_filter = ('recommended',)
    
