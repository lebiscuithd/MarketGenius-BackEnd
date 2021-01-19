from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_image = models.ImageField(blank=True, null=True)
    product_thumbnail = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.product_name


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    products = models.ManyToManyField(Product, through='ReceiptProduct')

    def __str__(self):
        return str(self.id)


class ReceiptProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.IntegerField()
