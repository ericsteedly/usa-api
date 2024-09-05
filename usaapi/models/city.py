from django.db import models
from .state import State

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    population = models.IntegerField()