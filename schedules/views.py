from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.exceptions import ValidationError
from users.models import User

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

    def perform_create(self, serializer):
        today = serializer.validated_data['date']
        count_today = Schedule.objects.filter(date=today).count()
        if count_today >= 5:
            raise ValidationError({
                "success": False,
                "message": "Schedule limit exceeded.",
                "errorDetails": {
                    "field": "date",
                    "message": "Cannot create more than 5 schedules per day."
                }
            })
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "success": True,
            "statusCode": 201,
            "message": "Schedule created successfully",
            "data": response.data
        }, status=status.HTTP_201_CREATED)
