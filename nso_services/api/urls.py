from netbox.api.routers import NetBoxRouter
from .views import NSOServiceViewSet, NSOServiceInstanceViewSet

router = NetBoxRouter()
router.register('services', NSOServiceViewSet)
router.register('instances', NSOServiceInstanceViewSet)

urlpatterns = router.urls