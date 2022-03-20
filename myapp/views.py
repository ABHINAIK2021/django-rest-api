from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Purchase
from myapp.serializers import PurchaseSerializer 

class PurchaseView(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()