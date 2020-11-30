from rest_framework import routers
from .api import LeadViewSet, ClassNameViewSet, StudentsViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/classname', ClassNameViewSet, 'class')
router.register('api/students', StudentsViewSet, 'Students')

urlpatterns = router.urls