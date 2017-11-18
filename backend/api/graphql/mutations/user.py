import graphene
from api.graphql.types.user import UserType
from django.contrib.auth.models import User as UserModel


class ChangeUserMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()

    errors = graphene.List(graphene.String)
    user = graphene.Field(lambda: UserType)

    @staticmethod
    def mutate(root, info, **kwargs):
        user = None
        errors = []
        if not UserModel.objects.filter(pk=kwargs.get('pk')).exists():
            errors.append('User does not exists')
        else:
            user = UserModel.objects.filter(pk=kwargs.get('pk')).get()

        if errors:
            return ChangeUserMutation(errors=errors, user=user)

        if kwargs.get('first_name'):
            user.first_name = kwargs.get('first_name')

        if kwargs.get('last_name'):
            user.last_name = kwargs.get('last_name')

        if kwargs.get('password'):
            if len(kwargs.get('password')) < 6:
                errors.append('Password should contains 6+ char')
            else:
                user.set_password(kwargs.get('password'))

        user.save()

        if kwargs.get('email'):
            if UserModel.objects.filter(email=kwargs.get('email')).exists():
                errors.append('User with email {} already exists'.format(
                    kwargs.get('email')
                ))
            else:
                user.email = kwargs.get('email')
                user.save()

        if kwargs.get('username'):
            if (
                UserModel.objects.filter(
                    username=kwargs.get('username')).exists()
            ):
                errors.append('User with username {} already exists'.format(
                    kwargs.get('username')
                ))
            else:
                user.username = kwargs.get('username')
                user.save()

        return ChangeUserMutation(errors=errors, user=user)
