from django.contrib.admin import ModelAdmin, site
from viewer.models import Genre, Movie


class MovieAdmin(ModelAdmin):
    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description="")

    # ordering = ['id']
    # list_display = ['id', 'title', 'genre', 'released_year']
    # list_display_links = ['id', 'title']
    # list_per_page = 10
    # list_filter = ['genre']
    # search_fields = ['title']
    # actions = ['cleanup_description']
    #
    # fieldsets = [
    #     ('Main info', {'fields': ['title', 'created'], 'description': 'Main information about the movie'}),
    #     ('External Information', {'fields': ['genre', 'released'], 'description': 'These fields are going to be filled with data parsed from external databases'}),
    #     ('User Information', {'fields': ['rating', 'description'], 'description': 'These fields are intended to be filled by our users'})
    # ]
    # readonly_fields = ['created']


site.register(Genre)
site.register(Movie, MovieAdmin)
