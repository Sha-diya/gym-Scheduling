from django.urls import path
from .views import ScheduleListCreateView

urlpatterns = [
    path('', ScheduleListCreateView.as_view(), name='schedule-list-create'),
]
