from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=15)


class Attendance(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    excused = models.BooleanField(default=False)


class Event(models.Model):
    type = models.ForeignKey('EventType', on_delete=models.CASCADE)
    date = models.DateField


class Department(models.Model):
    name = models.CharField(max_length=15)


class EventType(models.Model):
    name = models.CharField(max_length=15)
