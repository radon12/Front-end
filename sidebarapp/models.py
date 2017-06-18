from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_logo = models.CharField(max_length=400)
    movie_date = models.CharField(max_length=5)
    movie_genre = models.CharField(max_length=300)

    def __str__(self):
        return self.movie_title
