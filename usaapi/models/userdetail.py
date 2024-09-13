from django.db import models
from django.contrib.auth.models import User
from .state import State

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    home_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='home_state_users')
    visited_states = models.ManyToManyField(
        "State",
        through="StateVisit",
        related_name="user_details"
    )
