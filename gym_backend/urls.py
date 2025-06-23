from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    # Your existing app endpoints
    path('api/users/', include('users.urls')),
    path('api/schedules/', include('schedules.urls')),
    path('api/bookings/', include('bookings.urls')),

    # ✅ Add these two lines for token auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
