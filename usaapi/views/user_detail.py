from rest_framework import serializers, status
from usaapi.models import UserDetail
from .state import StateSerializer
from django.contrib.auth.models import User




class UserDetailSerializer(serializers.ModelSerializer):
    visited_states = StateSerializer(many=True)
    home_state = StateSerializer(many=False)

    class Meta:
        model = UserDetail
        fields = [
            'id',
            'home_state',
            'visited_states'
        ]

class UserSerializer(serializers.ModelSerializer):
    user_detail = UserDetailSerializer(many=False)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'user_detail'
        ]