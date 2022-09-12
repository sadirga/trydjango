from django.db import models

"""
whenever we make changes in models.py
always remember to:
1. run python manage.py makemigrations
2. run python manage.py migrate
"""

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default='This is cool!')