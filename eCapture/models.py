from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def user_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'avatars/user_{0}.{1}'.format(instance.user.username, ext)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.DO_NOTHING)
    role = models.ForeignKey('Role', on_delete=models.DO_NOTHING, default=1)
    dob = models.DateField()
    image = models.ImageField(upload_to=user_image_path)
    finger_print = models.BinaryField(default=b"")

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
        return str(self.user) + " | " + str(self.event)


@receiver(post_save, sender=Attendance)
def notify_defaults(sender, instance, **kwargs):
    user = instance.user
    status = "Absent from"
    if (instance.present is False) & (instance.excused is True):
        status = "Excused from"
    elif instance.present:
        status = "Present at"
    user.email_user(
        "Your attendance status for {0}".format(instance.event),
        "This is to inform you that you were {0} the following university "
        "gathering: \n{1}".format(status, instance.event),
        "admin@covenantuniversity.edu.ng")
    if (instance.present == False) & (instance.excused == False):
        defaults = user.attendance_set.filter(present=False,
                                              excused=False).count()
        if defaults >= 3:
            user.email_user(
                "You have missed attendance {0} times!".format(defaults),
                "This is to inform you that you have been "
                "marked absent from university gatherings {0} "
                "times.".format(defaults), "admin@covenantuniversity.edu.ng")


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
