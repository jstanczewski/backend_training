from logging import getLogger

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from viewer.forms import MovieForm

LOGGER = getLogger()


class IndexView(TemplateView):
    template_name = 'index.html'


class MovieDetailsView(DetailView):
    template_name = "detail.html"
    model = Movie


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "movie_confirm_delete.html"
    model = Movie
    success_url = reverse_lazy("viewer:movies")


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "form.html"
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("viewer:movies")

    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data while updating a movie!")
        return super().form_valid(form)


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


# FormView -> CreateView
class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = MovieForm
    success_url = reverse_lazy("viewer:movie_create")

    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data!")
        return super().form_invalid(form)


def hello(request):
    s1 = request.GET.get("s1", "")
    user = request.user
    return render(
        request,
        template_name="hello.html",
        context={"adjectives": [s1, "beautiful", "wonderful", "great"], 'user': user},
    )
