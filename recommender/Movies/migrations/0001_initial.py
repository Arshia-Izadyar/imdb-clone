# Generated by Django 3.2 on 2023-06-12 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lib.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.PositiveSmallIntegerField(choices=[(1, 'Comedy'), (2, 'Drama'), (3, 'Horror'), (4, 'Action'), (6, 'Comic'), (5, 'Magic'), (7, 'Fantasy')], default=4)),
            ],
        ),
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('release_year', models.DateField()),
                ('plot', models.TextField()),
                ('director', models.CharField(max_length=40)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='Movies.genremodel')),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_list', to='Movies.moviemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, validators=[lib.validator.check_rate])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='Movies.moviemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to='Movies.moviemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
