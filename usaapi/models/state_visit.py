from django.db import models
from .state import State
from .user_detail import UserDetail

class StateVisit(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)