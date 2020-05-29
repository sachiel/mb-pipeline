import jsonfield

from django.db import models

from app.models import BaseModel


class TripPoint(BaseModel):
    class Meta:
        verbose_name = "Vehicle Trip Point"
        verbose_name_plural = "Vehicle Trip Point"

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

    address = models.CharField('Address', max_length=256, default='', blank=True)
    zipcode = models.CharField('Zip', max_length=32, default='', blank=True)
    county = models.CharField('County', max_length=128, default='', blank=True)
    city = models.CharField('City', max_length=128, default='', blank=True)

    is_georeversed = models.BooleanField('Is georeversed?', default=False)
    is_address_proccesed = models.BooleanField('Is Address Processed?', default=False)

    georeverse_data = jsonfield.JSONField(blank=True, null=True)
    cdmxapi_data = jsonfield.JSONField(blank=True, null=True)


