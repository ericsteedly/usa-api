from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from usaapi.models import State



class States(ViewSet):
    def list(self, request):

        try:
            states = State.objects.all()
            serialized_states = StateSerializer(states, many=True)
        except Exception as e:
            print(f"Error accessing state objects: {e}")

        return Response(serialized_states.data, status=status.HTTP_200_OK)
    
class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = [
            'id',
            'name',
            'code'
        ]