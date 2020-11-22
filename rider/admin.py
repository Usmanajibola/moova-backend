from django.contrib import admin
from .models import RideHistory, Rider, Ride

# Register your models here.

admin.site.register(Rider)
admin.site.register(RideHistory)
admin.site.register(Ride)