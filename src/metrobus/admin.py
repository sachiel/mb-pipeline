from django.contrib import admin

from .models import TripPoint


@admin.register(TripPoint)
class TripPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'vehicle_id', 'is_georeversed',
                    'is_address_proccesed', 'address', 'zipcode', 'county',
                    'city', 'position_latitude', 'position_longitude']

