from django.db import models


# Create your models here.
class Task(models.Model):
    # ID, Name, Speaker, Venue, Duration
    name = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    venue = models.TextField()
    duration = models.IntegerField()