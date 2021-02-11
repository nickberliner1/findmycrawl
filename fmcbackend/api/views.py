from django.shortcuts import render

from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    '''I have to write this because VSC won't shut up'''
    queryset = Event.objects.all().order_by('name')
    serializer_class = EventSerializer
