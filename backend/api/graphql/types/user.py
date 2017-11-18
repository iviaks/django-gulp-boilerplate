from django.contrib.auth.models import User as UserModel
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
