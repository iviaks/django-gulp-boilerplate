from django.contrib.auth.models import User as UserModel
from graphene_django import DjangoObjectType
import graphene


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(
        User, id=graphene.Int(),
        email=graphene.String(), username=graphene.String()
    )

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all()

    def resolve_user(self, info, **kwargs):

        if kwargs.get('id'):
            if UserModel.objects.filter(pk=kwargs.get('id')).exists():
                return UserModel.objects.get(pk=kwargs.get('id'))

        if kwargs.get('email'):
            if UserModel.objects.filter(email=kwargs.get('email')).exists():
                return UserModel.objects.get(email=kwargs.get('email'))

        if kwargs.get('username'):
            if (
                UserModel.objects.filter(
                    username=kwargs.get('username')).exists()
            ):
                return UserModel.objects.get(username=kwargs.get('username'))

        return None


schema = graphene.Schema(query=Query)
