model (ORM) -> tabele w DB

python manage.py makemigrations
python manage.py migrate

1. (Create) Utworzyć rekordy
   Movie.objects.create(title='something', ...)
   film = Movie.objects(title='something', ...) -> film.save()
2. (Retrieve) Pobrać (jeden, wiele) rekordów na podstawie np. filtrowania itp.
Movies.objects.filter(rating__gte=6).filter(title__icontains='and')
   Model objects.get(...) -> zwraca 1 obiekt
   Model.objects.filter(...) -> zwraca QuerySet (specyficzną listę obiektów/rekordów)
3. (Update) Modyfikacja rekordu
4. (Delete) Usuwanie rekordu
CRUD - Create, Retrieve, Update, Delete

The Lord of the Rings, 2001, Fantasy
One Flew Over the Cuckoo's Nest, 1975, Drama
Django, 2012, Western
Pulp Fiction, 1994, Drama
The Shawshank Redemption, 1994, Drama
Fight Club, 1999, Drama
