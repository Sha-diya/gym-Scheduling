# schedules/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Schedule
from .serializers import ScheduleSerializer
from datetime import datetime, timedelta

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class ScheduleListCreateView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'trainer':
            return Schedule.objects.filter(trainer=user)
        return Schedule.objects.all()

    def perform_create(self, serializer):
        start = serializer.validated_data['start_time']
        end = serializer.validated_data['end_time']
        date = serializer.validated_data['date']

        if Schedule.objects.filter(date=date).count() >= 5:
            raise ValidationError({"message": "Cannot schedule more than 5 classes per day."})

        start_dt = datetime.combine(datetime.today(), start)
        end_dt = datetime.combine(datetime.today(), end)
        if end_dt - start_dt != timedelta(hours=2):
            raise ValidationError({"message": "Each class must last exactly 2 hours."})

        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "success": True,
            "statusCode": 201,
            "message": "Schedule created successfully",
            "data": response.data
        }, status=status.HTTP_201_CREATED)
