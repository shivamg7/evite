from rest_framework import serializers
from .models import event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ('name', 'startDate', 'endDate', 'city','Venue','category','ticketPrice','image','description')