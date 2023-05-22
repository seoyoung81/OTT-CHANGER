from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Provider(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    m_id = models.BigAutoField(primary_key=True)
    id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.DateField()
    backdrop_path = models.TextField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre)
    providers = models.ManyToManyField(Provider, related_name='providers')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


# class Review(models.Model):
#     content = models.TextField()
#     movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="reviews")
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
