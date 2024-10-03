from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from usaapi.models import StateVisit
from .user_detail import UserDetailSerializer
from .state import StateSerializer


class StateVisits(ViewSet):
    def list(self, request):
        state_visits = StateVisit.objects.all()
        serialized_visits = StateVisitSerializer(state_visits, many=True)

        return Response(serialized_visits.data, status=status.HTTP_200_OK)


class StateVisitSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(many=False)
    state = StateSerializer(many=False)

    class Meta:
        model = StateVisit
        fields = [
            'id',
            'user',
            'state'
        ]
