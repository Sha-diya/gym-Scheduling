# gym_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/schedules/', include('schedules.urls')),
    path('api/bookings/', include('bookings.urls')),
]
