from django.contrib import admin

from .models import Airport, NjaFlight, Passenger

# Register your models here.
admin.site.register(Airport)
admin.site.register(NjaFlight)
admin.site.register(Passenger)
