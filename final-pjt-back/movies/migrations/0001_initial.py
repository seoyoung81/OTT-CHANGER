# Generated by Django 3.2.18 on 2023-05-23 00:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('m_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('poster_path', models.TextField()),
                ('release_date', models.DateField()),
                ('backdrop_path', models.TextField()),
                ('popularity', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('providers', models.ManyToManyField(related_name='providers', to='movies.Provider')),
            ],
        ),
    ]
