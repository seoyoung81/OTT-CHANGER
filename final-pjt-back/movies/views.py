from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
import random

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

# 이용중인 ott의 영화 추천
@api_view(['GET', 'POST'])
def movie_list(request):
    # print('>>>>>>>>>>>>>>>.')
    ott_pk = request.data['pk']
    movies = Movie.objects.all()
    movie_lst = []
    for i in range(len(movies)):
        providers = movies[i].providers.all()
        for j in range(len(providers)):
            if providers[j].pk == ott_pk:
                movie_lst.append(movies[i])
    serializer = MovieListSerializer(movie_lst, many=True)
    return Response(serializer.data)

# 장르 유사도 추천 알고리즘
@api_view(['GET'])
def recommend_genre(request):
    pass


# 영화 랜덤 추출 (ott 선택)
@api_view(['GET'])
def movie_select(request):
    movies = get_list_or_404(Movie)
    movie_lst = []
    for i in range(len(movies)):
        providers = movies[i].providers.all()
        if len(providers) >= 3:
            movie_lst.append(movies.pop(i))
            if len(movie_lst) == 10:
                break
    
    lst = random.sample(movies, 30)
    movie_lst = movie_lst + lst
    serializer = MovieListSerializer(movie_lst, many=True)
    return Response(serializer.data)
    

@api_view(['GET', 'POST'])
def movie_search(request):
    movies = get_list_or_404(Movie)
    keyword = request.data['keyword']
    print('>>>>>>>>>>>>.')
    print(keyword)
    for movie in movies:
        if movie.title == keyword:
            result = movie
            break
    print(result)

    serializer = MovieListSerializer(result)
    return Response(serializer.data)

