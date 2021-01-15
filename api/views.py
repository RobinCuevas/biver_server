from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Invoice, Local
from .serializers import InvoiceSerializer

# Create your views here.

class InvoicesRestaurant (APIView):
    def get(self,request):
        #this function must show every invoice in the system
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
