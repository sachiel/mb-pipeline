import datetime
from django.core.management.base import BaseCommand, CommandError

from metrobus.models import Vehicle
from metrobus.services.cdmxapi import get_data as mb_fetch


class Command(BaseCommand):
    help = 'Fetch Metrobus Data from datos.cdmx.gob.mx'

    def handle(self, *args, **options):
        # get data from api
        mb_data = mb_fetch()

        if not mb_data:
            raise CommandError("Can't retrieve data from CDMX API")

        for record in mb_data:
            obj, created = Vehicle.objects.get_or_create(
                    record_id=record['recordid'],
            )

            if created and 'fields' in record:
                fields = record['fields']
                trip_start_date = fields.get('trip_start_date', None)

                if trip_start_date:
                    trip_start_date = datetime.datetime.strptime(trip_start_date, '%Y%m%d')

                obj.vehicle_id = fields.get('vehicle_id', '')
                obj.trip_id = fields.get('trip_id', '')
                obj.trip_route_id = fields.get('trip_route_id', '')
                obj.trip_schedule_relationship = fields.get('trip_schedule_relationship', '')
                obj.vehicle_label = fields.get('vehicle_label', '')
                obj.vehicle_current_status = fields.get('vehicle_current_status', 0)
                obj.position_longitude = fields.get('position_longitude', '')
                obj.position_latitude = fields.get('position_latitude', '')
                obj.position_speed = fields.get('position_speed', 0)
                obj.position_odometer = fields.get('position_odometer', 0)
                obj.trip_start_date = trip_start_date 
                obj.date_updated = fields.get('date_updated', None)

                obj.save()

