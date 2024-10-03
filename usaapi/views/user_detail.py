from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
    user_detail = UserDetailSerializer(source='userdetail', many=False)

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

class UserDetails(ViewSet):

    def list(self, request):
        user_details = UserDetail.objects.get(user=request.auth.user)
        user = User.objects.get(pk=user_details.id)

        serialized_user = UserSerializer(user, many=False, context={"request": request})

        return Response(serialized_user.data, status=status.HTTP_200_OK)