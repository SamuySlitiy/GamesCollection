import os
import django

os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="games_collection.settings")
django.setup()

