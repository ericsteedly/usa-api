from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from usaapi.models import City
from .state import StateSerializer

class Cities(ViewSet): 
    def list(self, request):

        cities = City.objects.all()
        serialized_cities = CitySerilaizer(cities, many=True)

        return Response(serialized_cities.data, status=status.HTTP_200_OK)


class CitySerilaizer(serializers.ModelSerializer):
    state = StateSerializer(many=False)
    class Meta:
        model = City
        fields = [
            'id',
            'name',
            'state',
            'population'
        ]