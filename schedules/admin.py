from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'start_time', 'end_time', 'trainer')
    list_filter = ('date', 'trainer')
    search_fields = ('trainer__username', 'date')
