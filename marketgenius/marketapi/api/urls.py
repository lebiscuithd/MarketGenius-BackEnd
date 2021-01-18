from django.conf.urls import url, include
from .views import ProductViewSet, TicketViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"tickets", TicketViewSet, basename="ticket")

urlpatterns = [
    url('', include(router.urls))
]