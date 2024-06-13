from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
   
    def validate_resume(self,value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many = True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_data', 'actors', 'rate', 'resume']

    def get_rate(self,obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate,1)
        return None

    
class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
