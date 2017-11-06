import graphene
from api.graphql.queries import UserQuery
from api.graphql.mutations import ChangeUserMutation


class Mutation(graphene.ObjectType):
    changeUser = ChangeUserMutation.Field()


class Query(UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
