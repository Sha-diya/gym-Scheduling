from django.db import models
from users.models import User

class Schedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'trainer'})

    def __str__(self):
        return f"{self.date} - {self.start_time} ({self.trainer})"
