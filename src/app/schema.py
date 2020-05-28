import graphene

import metrobus.schema

class Query(metrobus.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

