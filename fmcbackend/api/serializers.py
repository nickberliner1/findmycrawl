from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'main_picture', 'description', 'comes_with_free_drinks', 'start_time')