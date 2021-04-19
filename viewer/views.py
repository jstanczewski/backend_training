from logging import getLogger
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from viewer.forms import MovieForm

LOGGER = getLogger()


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


class MovieCreateView(FormView):
    template_name = "form.html"
    form_class = MovieForm
    success_url = reverse_lazy("movie_create")

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data["title"],
            genre=cleaned_data["genre"],
            rating=cleaned_data["rating"],
            released=cleaned_data["released"],
            description=cleaned_data["description"],
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning("User provided and invalid data!")
        return super().form_invalid(form)


# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all().order_by('-rating'),
#                      'title': "Wynik TemplateView"}


# class MoviesView(View):
#     def get(self, request):
#         return render(
#             request, template_name='movies.html',
#             context={'movies': Movie.objects.all().order_by('-rating')}
#         )


# def movies(request):
#     return render(
#         request, template_name='movies.html',
#         context={'movies': Movie.objects.all().order_by('-rating')}
#     )


def hello(request):
    s1 = request.GET.get("s1", "")
    return render(
        request,
        template_name="hello.html",
        context={"adjectives": [s1, "beautiful", "wonderful", "great"]},
    )

    # try:
    #     s = int(request.GET.get('s', ''))
    # except Exception as ex:
    #     return HttpResponse(f'Something went wrong! Error: {ex}')
    # text = f'<b>Given value =  {s}</b><br>' \
    #     f"<a href='/hello/?s={s+1}'>Add 1</a><br>" \
    #     f"<a href='/hello/?s={s-1}'>Subtract 1</a>"
    # return HttpResponse(text)
