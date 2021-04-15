from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from viewer.forms import MovieForm


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm


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
