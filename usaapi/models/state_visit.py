from django.db import models
from .state import State
from .userdetail import UserDetail

class StateVisit(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    user_detail = models.ForeignKey(UserDetail, on_delete=models.CASCADE)