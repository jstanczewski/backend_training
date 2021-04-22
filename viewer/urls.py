from django.urls import path
from viewer.views import (
    MoviesView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    MovieDetailsView,
)

app_name = "viewer"

urlpatterns = [
    path("movies/", MoviesView.as_view(), name="movies"),
    path("movies/create/", MovieCreateView.as_view(), name="movie_create"),
    path("movies/<int:pk>/", MovieDetailsView.as_view(), name="movie_details"),
    path("movies/update/<int:pk>/", MovieUpdateView.as_view(), name="movie_update"),
    path("movies/delete/<int:pk>/", MovieDeleteView.as_view(), name="movie_delete"),
]
