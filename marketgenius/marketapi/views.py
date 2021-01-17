from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer, TicketSerializer
from .models import Product, Ticket


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        ticket = Ticket.objects.all()
        return ticket     