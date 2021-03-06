from rest_framework import serializers
from marketapi.models import Product, Ticket, ReceiptProduct, Promotion


class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ['id', 'promotion_remise', 'promotion_free', 'promotion_name']

class ReceiptProductSerializer(serializers.HyperlinkedModelSerializer):

    product_name = serializers.ReadOnlyField(source='product.product_name')
    product_price = serializers.ReadOnlyField(source='product.product_price')

    class Meta:
        model = ReceiptProduct

        fields = ('product_name', 'product_price', 'quantity')


class ProductSerializer(serializers.ModelSerializer):

    product_promotion = PromotionSerializer()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_price', 'product_thumbnail', 'product_promotion']


class TicketSerializer(serializers.ModelSerializer):

    products = ReceiptProductSerializer(source='receiptproduct_set', many=True)

    class Meta:
        model = Ticket
        fields = ['id', 'created_at', 'total_price', 'products']
        depth = 1
