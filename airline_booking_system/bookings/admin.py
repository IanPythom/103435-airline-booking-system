from django.contrib import admin
from .models import Flight, Passenger  # Import your models

admin.site.register(Flight)
admin.site.register(Passenger)
