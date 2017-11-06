from rest_framework import routers
from api.rest.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
