from django.conf.urls import url, include
from graphene_django.views import GraphQLView
from rest_framework import routers
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [

    # REST API
    url(r'^v1/rest-auth/', include('rest_auth.urls')),
    url(
        r'^v1/rest-auth/registration/',
        include('rest_auth.registration.urls')
    ),

    # GraphQL API
    url(r'^v1/', include(router.urls)),
    url(r'^v2/', GraphQLView.as_view(graphiql=True), name='graphql')
]
