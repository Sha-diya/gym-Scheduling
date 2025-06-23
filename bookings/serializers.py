from rest_framework import serializers
from .models import Booking
from users.models import User
from schedules.models import Schedule

class BookingSerializer(serializers.ModelSerializer):
    trainee_name = serializers.ReadOnlyField(source='trainee.username')
    class Meta:
        model = Booking
        fields = ['id', 'schedule', 'trainee', 'trainee_name', 'booked_at']
