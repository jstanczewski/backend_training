from django.contrib.admin import ModelAdmin, site
from viewer.models import Genre, Movie


class MovieAdmin(ModelAdmin):
    list_display = ['id', 'title', 'genre']


site.register(Genre)
site.register(Movie, MovieAdmin)
