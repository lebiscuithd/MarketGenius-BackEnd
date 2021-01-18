from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer, TicketSerializer
from marketapi.models import Product, Ticket, ReceiptProduct


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

    def create(self, request, *args, **kwargs): 
        data = request.data

        new_ticket = Ticket.objects.create(
            total_price=data["total_price"])

        new_ticket.save()
        
        new_ticket_id = Ticket.objects.last().id

        for receiptproduct in data["products"]:
            new_receiptproduct = ReceiptProduct.objects.create(
                quantity=receiptproduct["quantity"], product_id=receiptproduct["product_id"], ticket_id=new_ticket_id)

            new_receiptproduct.save() 

        serializer = TicketSerializer(new_ticket)
        return Response(serializer.data)    