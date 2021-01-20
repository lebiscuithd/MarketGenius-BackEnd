from django.contrib import admin
from .models import Product, Ticket, ReceiptProduct, Promotion

admin.site.register(Product)
admin.site.register(Ticket)
admin.site.register(ReceiptProduct)
admin.site.register(Promotion)
