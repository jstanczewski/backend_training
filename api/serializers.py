from viewer.models import Movie, Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    # genre = GenreSerializer(many=False, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
        excluded = ["created"]
