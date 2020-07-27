from django.db import models
from django.contrib.auth.models import User


def user_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'avatars/user_{0}.{1}'.format(instance.user.username, ext)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.DO_NOTHING)
    role = models.ForeignKey('Role', on_delete=models.DO_NOTHING, default=1)
    image = models.ImageField(upload_to=user_image_path)

    def __str__(self):
        return str(self.user)


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    excused = models.BooleanField(default=False)

    def __str__(self):
        return str(self.event)

class Event(models.Model):
    type = models.ForeignKey('EventType', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return str(self.type) + " - " + str(self.date)


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
