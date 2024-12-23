from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('passengers', PassengerViewSet)

urlpatterns = router.urls
