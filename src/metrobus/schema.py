import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from metrobus.services.app import get_all_cities, get_all_vehicles

from .models import TripPoint


class VehicleType(graphene.ObjectType):
    id = graphene.String()
    label = graphene.String()


class CityType(graphene.ObjectType):
    name = graphene.String()


class TripPointType(DjangoObjectType):
    class Meta:
        model = TripPoint
        fields = [
            'id',
            'vehicle_id',
            'address',
            'city',
            'date_updated',
        ]


class VehicleNode(DjangoObjectType): 
    class Meta:
        model = TripPoint
        fields = [
            'id',
            'vehicle_id',
            'vehicle_label',
            'address',
            'county',
            'zipcode',
            'city',
            'date_updated',
        ]
        filter_fields = ['city', 'zipcode', 'vehicle_id',]
        interfaces = (graphene.relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.exclude(is_address_proccesed=False)


class Query(object):
    all_trippoints = graphene.List(TripPointType)
    all_cities = graphene.List(CityType)
    all_vehicles_availables  = graphene.List(VehicleType)

    vehicle = graphene.relay.Node.Field(VehicleNode)
    all_vehicles = DjangoFilterConnectionField(VehicleNode)

    def resolve_all_vehicles_availables(self, info, **kwargs):
        return get_all_vehicles()

    def resolve_all_cities(self, info, **kwargs):
        return get_all_cities() 

    def resolve_all_trippoints(self, info, **kwargs):
        return TripPoint.objects.filter(is_address_proccesed=True)


