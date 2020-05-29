import json

from metrobus.models import TripPoint


def get_all_cities():
    """ Search in database all cities availables, return a list:
        [
            {"name": "Benito Juarez"},
            ...
        ]
    """
    
    objects_list = TripPoint.objects.filter(
        is_address_proccesed=True
    ).values('city').distinct()

    return [{'name': obj['city']} for obj in objects_list]


def get_all_vehicles():
    """ Search in database all vehicles availables, return a list:
        [
            {"id": "1234", "label": "5678"},
            ...
        ]
    """
    objects_list = TripPoint.objects.filter(
        is_address_proccesed=True
    ).values('vehicle_id', 'vehicle_label').distinct()

    return [
        {'id': obj['vehicle_id'], 'label': obj['vehicle_label']} \
            for obj in objects_list
    ]


