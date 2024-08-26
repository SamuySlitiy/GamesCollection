from django.db import models

# Create your models here.

from django.db import models

# Модель для жанрів ігор
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель для ігор
class Game(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # Наприклад, рейтинг від 0.0 до 10.0
    genres = models.ManyToManyField(Genre, related_name='games')

    def __str__(self):
        return self.title