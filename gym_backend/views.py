# example: gym_backend/views.py (create this file if needed)

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Gym Scheduling API"})
