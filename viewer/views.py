from logging import getLogger
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import render
from django.urls import reverse_lazy
from viewer.models import Movie
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from viewer.forms import MovieForm

LOGGER = getLogger()


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class NameRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return self.request.user.first_name != "" and user.last_name != ""


class IndexView(TemplateView):
    template_name = "index.html"


class MovieDetailsView(DetailView):
    template_name = "detail.html"
    model = Movie


class MovieDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = "movie_confirm_delete.html"
    model = Movie
    success_url = reverse_lazy("viewer:movies")
    permission_required = "viewer.delete_movie"

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "form.html"
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("viewer:movies")
    permission_required = "viewer.change_movie"

    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data while updating a movie!")
        return super().form_valid(form)


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


class MovieCreateView(NameRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = MovieForm
    success_url = reverse_lazy("viewer:movie_create")
    permission_required = "viewer.add_movie"

    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data!")
        return super().form_invalid(form)


def hello(request):
    s1 = request.GET.get("s1", "")
    user = request.user
    return render(
        request,
        template_name="hello.html",
        context={"adjectives": [s1, "beautiful", "wonderful", "great"], "user": user},
    )
