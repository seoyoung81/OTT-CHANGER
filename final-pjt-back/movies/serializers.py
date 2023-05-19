from rest_framework import serializers
from .models import Genre, Provider, Movie

# Providers 정보 제공
class ProviderList(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class GenreList(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


# OTT 영화 전체 리스트 제공(모든 정보 제공)
class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


# OTT 단일 영화 리스트 제공 (Provider 정보만 제공) -> 알고리즘 짤 때 provider 개수 확인할 때 사용
class MovieDetailProviderSerializer(serializers.ModelSerializer):
    providers = ProviderList(many=True, read_only=True, source="provider_id")
    
    class Meta:
        model = Movie
        fields = ('provider_id')
  
# OTT 단일 영화 리스트 제공 (genre 정보만 제공)        
class MovieDetailGenreSerializer(serializers.ModelSerializer):
    genres = GenreList(many=True, read_only=True, source="genre_id")
    
    class Meta:
        model = Movie
        fields = ('genre_id')