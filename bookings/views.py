# bookings/views.py
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

    def get_queryset(self):
        user = self.request.user
        if user.role == 'trainee':
            return Booking.objects.filter(trainee=user)
        elif user.role == 'trainer':
            return Booking.objects.filter(schedule__trainer=user)
        elif user.role == 'admin':
            return Booking.objects.all()
        return Booking.objects.none()

    def perform_create(self, serializer):
        schedule = serializer.validated_data['schedule']
        if schedule.bookings.count() >= 10:
            raise ValidationError({"message": "Class is full. Maximum 10 trainees allowed."})
        serializer.save(trainee=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "success": True,
            "statusCode": 201,
            "message": "Class booked successfully",
            "data": response.data
        }, status=status.HTTP_201_CREATED)
