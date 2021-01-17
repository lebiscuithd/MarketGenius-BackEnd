from django.conf.urls import url, include
from .views import ProductViewSet, TicketViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("product", ProductViewSet, basename="product")
router.register("ticket", TicketViewSet, basename="ticket")

urlpatterns = [
    url('', include(router.urls))
]