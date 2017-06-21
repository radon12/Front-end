from django.db import models

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

class User(models.Model):
    username = models.CharField(max_length=100)
    password = 'default'

    def __str__(self):
        return self.username

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    userid = models.CharField(max_length=10)
    rating = models.FloatField()

    def __str__(self):
        return self.movie.movie_title + self.userid + " " + str(self.rating)
