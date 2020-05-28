import json

from metrobus.models import TripPoint


def get_all_cities():
    """
    return [
        {"name": "Uno"},
        {"name": "Dos"},
        {"name": "Tres"},
        {"name": "Cuarenta"},
    ]
    """
    
    objects_list = TripPoint.objects.filter(
        is_address_proccesed=True
    ).values('city').distinct()

    return [{'name': obj['city']} for obj in objects_list]


def get_all_vehicles():
    """
    return [
        {"name": "Uno"},
        {"name": "Dos"},
        {"name": "Tres"},
        {"name": "Cuarenta"},
    ]
    """
    objects_list = TripPoint.objects.filter(
        is_address_proccesed=True
    ).values('vehicle_id', 'vehicle_label').distinct()

    return [
        {'id': obj['vehicle_id'], 'label': obj['vehicle_label']} \
            for obj in objects_list
    ]


