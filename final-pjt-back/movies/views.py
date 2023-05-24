from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
import random

from .models import Genre, Provider, Movie
from accounts.models import User
from .serializers import ProviderList, GenreList, MovieListSerializer, MovieDetailProviderSerializer, MovieDetailGenreSerializer, MovieLikeUsers


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
    # print('>>>>>>>>>>>>.')
    # print(keyword)
    for movie in movies:
        if movie.title == keyword:
            result = movie
            break
    # print(result)

    serializer = MovieListSerializer(result)
    return Response(serializer.data)

# 영화 좋아요
@api_view(['GET', 'POST'])
def movie_like(request, movie_pk):
    if request.method == 'GET':
        print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
        movie = get_object_or_404(Movie, m_id=movie_pk)
        print(movie_pk)
        print(movie)
        likes_count = movie.like_users.count()
        print(likes_count)
        print('잘 갔니..?')
        return Response({'likes_count': likes_count})


    if request.method == 'POST':
        print('11111111111111111')
        like_movie = request.data['like_movie']
        like_user = User.objects.get(pk=request.data['user_pk'])
        movies = Movie.objects.all()
        try:
            print('222222222222222222')
            movie = Movie.objects.get(id=like_movie['id'])
        except:
            print('333333333333333333')
            movie = Movie()
            movie.m_id = len(movies) + 1
            movie.id = like_movie['id']
            movie.title = like_movie['title']
            movie.overview = like_movie['overview']
            movie.poster_path = like_movie['poster_path']
            movie.release_date = like_movie['release_date']
            movie.backdrop_path = like_movie['backdrop_path']
            movie.popularity = like_movie['popularity']
            movie.vote_count = like_movie['vote_count']
            movie.vote_average = like_movie['vote_average']
            print(movie)
            print(like_movie['genre_ids'])
            # movie.genres = list(like_movie['genre_ids'])
            # print(movie)
            movie.save()
            print(movie)
            
            # Get Genre objects based on genre_ids
            genre_ids = like_movie['genre_ids']
            genres = Genre.objects.filter(pk__in=genre_ids)

            # Clear existing genres and add new ones
            movie.genres.clear()
            movie.genres.add(*genres)

        finally:
            if movie.like_users.filter(pk=like_user.pk).exists():
                movie.like_users.remove(like_user.pk)
                print('remove like user')
            else:
                movie.like_users.add(like_user.pk)
                print('add like user')

        serializer = MovieLikeUsers(movie)
        # print(serializer.data)   
        return Response(serializer.data)
        
 

@api_view(['GET'])
def movie_detail(request, movie_pk):
# print('>>>>>>>>>>>>>>>.')
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieLikeUsers(movie)
    return Response(serializer.data)

   
# 내가 좋아요한 영화 조회
@api_view(['GET'])
def my_movie_likes(request, user_pk):
    like_lst = []
    movies = get_list_or_404(Movie)
    print(user_pk)
    for movie in movies:
        if movie.like_users.filter(pk=user_pk).exists():
            like_lst.append(movie)

    serializer = MovieListSerializer(like_lst, many=True)
    return Response(serializer.data)

   
   
   
   
   
   
   