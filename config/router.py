from rest_framework import routers

from myuser.api.views import AccountViewSet
from fix.api.views import FixViewSet, RecruitViewSet
from project.api.views import OpenSourceProjectViewSet, ToolViewSet
from blog.api.views import BlogViewSet

router = routers.DefaultRouter()
router.register(r'user', AccountViewSet)
router.register(r'project/open_source', OpenSourceProjectViewSet)
router.register(r'project/tools', ToolViewSet)
router.register(r'blog/user', BlogViewSet, base_name='blog')
router.register(r'fix/recruit', RecruitViewSet, base_name='recruit')
router.register(r'fix', FixViewSet)
