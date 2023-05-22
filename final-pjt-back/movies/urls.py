from django.urls import path
from . import views

urlpatterns = [
    path('provider/', views.provider_list),
    path('provider/<int:provider_pk>/', views.provider_detail),
    path('genre/', views.genre_list),
    path('genre/<int:genre_pk>/', views.genre_detail),
    path('movies/', views.movie_list),
    # 장르 기반 추천 알고리즘 (장르 유사도)
    path('recommend_genre/', views.recommend_genre),
    path('movie_select/', views.movie_select),
    path('movie_search/', views.movie_search),
    path('movie_like/', views.movie_like),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/likes/<int:user_pk>/', views.my_movie_likes),
    
]
