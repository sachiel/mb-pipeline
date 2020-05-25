from django.db import models

from app.models import BaseModel


class Vehicle(BaseModel):
    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return "{}".format(
            self.vehicle_label
        )


    record_id = models.CharField('Record ID', max_length=128)
    vehicle_id = models.CharField('Vehicle ID', max_length=64, default="", blank=True)
    trip_id = models.CharField('Trip ID', max_length=64, default="", blank=True)
    trip_route_id = models.CharField('Trip Route ID', max_length=64, default="", blank=True)

    trip_schedule_relationship = models.CharField(
        'Trip Schedule Relationship', max_length=64, default="", blank=True
    )

    vehicle_label = models.CharField('Vehicle Label', max_length=64, default="", blank=True)
    vehicle_current_status = models.SmallIntegerField('Vehicle Current Status', default=0)

    position_longitude = models.CharField(
        'Trip Schedule Relationship', max_length=64, default="", blank=True
    )
    position_latitude = models.CharField(
        'Trip Schedule Relationship', max_length=64, default="", blank=True
    )
    position_speed = models.FloatField('Vehicle Current Status', default=0)
    position_odometer = models.FloatField('Vehicle Current Status', default=0)

    trip_start_date = models.DateField('Start Trip Date', blank=True, null=True)
    date_updated = models.DateTimeField('Record Update', blank=True, null=True)

    is_georeversed = models.BooleanField('Is georeversed?', default=False)


