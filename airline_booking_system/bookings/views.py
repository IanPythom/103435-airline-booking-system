from rest_framework import viewsets, filters
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer
from django_filters.rest_framework import DjangoFilterBackend

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['origin', 'destination', 'departure']
    ordering_fields = ['departure', 'arrival']

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['flight']
