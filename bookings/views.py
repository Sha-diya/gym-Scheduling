from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Booking
from .serializers import BookingSerializer
from schedules.models import Schedule

class IsTrainee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'trainee'

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsTrainee()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        schedule = serializer.validated_data['schedule']
        if schedule.bookings.count() >= 10:
            raise ValidationError({"message": "Class schedule is full. Maximum 10 trainees allowed per schedule."})
        serializer.save(trainee=self.request.user)

    # ✅ Custom success response
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "success": True,
            "statusCode": status.HTTP_201_CREATED,
            "message": "Class booked successfully",
            "data": response.data
        }, status=status.HTTP_201_CREATED)
