from django.db import models
from users.models import User
from schedules.models import Schedule

class Booking(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='bookings')
    trainee = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'trainee'})
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trainee.username} booked {self.schedule}"
