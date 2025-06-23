from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "success": True,
            "statusCode": 201,
            "message": "User registered successfully",
            "data": response.data
        }, status=status.HTTP_201_CREATED)
