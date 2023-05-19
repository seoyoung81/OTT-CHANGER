from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Genre, Provider, Movie
from .serializers import ProviderList, GenreList, MovieListSerializer, MovieDetailProviderSerializer, MovieDetailGenreSerializer


@api_view(['GET'])
def provider_list(request):
    providers = Provider.objects.all()
    serializer = ProviderList(providers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def provider_detail(request, provider_pk):
    provider = Provider.objects.get(pk=provider_pk)
    serializer = ProviderList(provider)
    return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreList(genres, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genre_detail(request, genre_pk):
    genres = Genre.objects.get(pk=genre_pk)
    serializer = GenreList(genres)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 장르 유사도 추천 알고리즘
@api_view(['GET'])
def recommend_genre(request):
    pass