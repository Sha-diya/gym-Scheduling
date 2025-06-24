# bookings/serializers.py
from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    trainee_name = serializers.ReadOnlyField(source='trainee.username')

    class Meta:
        model = Booking
        fields = ['id', 'schedule', 'trainee', 'trainee_name', 'booked_at']
