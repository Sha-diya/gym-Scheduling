# bookings/admin.py
from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'trainee', 'schedule', 'booked_at')
    list_filter = ('booked_at', 'schedule')
    search_fields = ('trainee__username', 'schedule__date')
