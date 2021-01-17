from rest_framework import serializers
from marketapi.models import Product, Ticket

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_price']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'created_at', 'total_price', 'products']
        depth = 1