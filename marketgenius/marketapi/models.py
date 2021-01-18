from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()

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
