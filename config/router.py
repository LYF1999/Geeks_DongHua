from rest_framework import routers

from myuser.api.views import AccountViewSet
from fix.api.views import FixViewSet

router = routers.DefaultRouter()
router.register(r'user', AccountViewSet)
router.register(r'fix', FixViewSet)
