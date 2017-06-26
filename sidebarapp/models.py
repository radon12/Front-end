from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""class client(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username"""


class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_logo = models.CharField(max_length=400)
    movie_date = models.CharField(max_length=5)
    movie_genre = models.CharField(max_length=300)

    def __str__(self):
        return self.movie_title

class oldUser(models.Model):
    username = models.CharField(max_length=100)
    password = 'default'

    def __str__(self):
        return self.username

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.movie.movie_title + " " + self.user.username+ " " + str(self.rating)
