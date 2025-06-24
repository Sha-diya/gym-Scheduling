# schedules/serializers.py
from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    trainer_name = serializers.ReadOnlyField(source='trainer.username')

    class Meta:
        model = Schedule
        fields = ['id', 'date', 'start_time', 'end_time', 'trainer', 'trainer_name']

