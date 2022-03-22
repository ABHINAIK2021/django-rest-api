from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Contact
from myapp.serializers import ContactSerializer 

class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()