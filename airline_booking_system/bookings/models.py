from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="passengers")
