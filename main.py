import django_settings
from collection.models import Game, Genre  # замініть 'myapp' на вашу назву додатку

# Створення жанрів
'''
genre1 = Genre(name="Action")
genre2 = Genre(name="Adventure")
genre3 = Genre(name="RPG")
genre4 = Genre(name="Strategy")

# Створення ігор і додання жанрів
game1 = Game(title="The Witcher 3: Wild Hunt", release_year=2015, rating=9.8)
game1.genres.add(genre3, genre2)

game2 = Game(title="Starcraft II", release_year=2010, rating=9.0)
game2.genres.add(genre4, genre1)

game3 = Game(title="God of War", release_year=2018, rating=9.7)
game3.genres.add(genre1, genre2)
'''

# Виведення доданих ігор
print(Game.objects.all())
