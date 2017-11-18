import graphene
from api.graphql.mutations.user import ChangeUserMutation
from api.graphql.queries.user import UserQuery


class Mutation(graphene.ObjectType):
    changeUser = ChangeUserMutation.Field()


class Query(UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
