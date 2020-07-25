from django.contrib import admin
from .models import Attendance, Department, Role, EventType, Event

admin.site.register(Attendance)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(EventType)
admin.site.register(Event)