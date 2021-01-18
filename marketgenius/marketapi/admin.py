from django.contrib import admin
from .models import Product, Ticket, ReceiptProduct

admin.site.register(Product)
admin.site.register(Ticket)
admin.site.register(ReceiptProduct)
