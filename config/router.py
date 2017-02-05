from rest_framework import routers

from myuser.api.views import AccountViewSet
from fix.api.views import FixViewSet
from project.api.views import OpenSourceProjectViewSet, ToolViewSet

router = routers.DefaultRouter()
router.register(r'user', AccountViewSet)
router.register(r'fix', FixViewSet)
router.register(r'project/open_source', OpenSourceProjectViewSet)
router.register(r'project/tools', ToolViewSet)
