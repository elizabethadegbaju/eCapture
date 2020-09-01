from django.contrib import admin
from .models import Attendance, Department, Role, EventType, Event, Staff, Capture

admin.site.register(Attendance)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(Staff)
admin.site.register(Capture)