from rest_framework import serializers
from marketapi.models import Product, Ticket, ReceiptProduct


class ReceiptProductSerializer(serializers.HyperlinkedModelSerializer):

    product_name = serializers.ReadOnlyField(source='product.product_name')
    product_price = serializers.ReadOnlyField(source='product.product_price')

    class Meta:
        model = ReceiptProduct

        fields = ('product_name', 'product_price', 'quantity')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_price']


class TicketSerializer(serializers.ModelSerializer):

    products = ReceiptProductSerializer(source='receiptproduct_set', many=True)

    class Meta:
        model = Ticket
        fields = ['id', 'created_at', 'total_price', 'products']
        depth = 1
