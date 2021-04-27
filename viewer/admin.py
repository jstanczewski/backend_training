from django.contrib.admin import ModelAdmin, site
from viewer.models import Genre, Movie


class MovieAdmin(ModelAdmin):
    @staticmethod
    def released_year(obj):
        return obj.released.year

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 10
    list_filter = ['genre']


site.register(Genre)
site.register(Movie, MovieAdmin)
