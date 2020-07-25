from django.shortcuts import render
from django.views import generic
from .models import Attendance, User


def index(request):
    return render(request, 'eCapture/index.html')


class DefaultsView(generic.ListView):
    model = Attendance
    template_name = 'eCapture/defaults.html'


class ProfileSettingsView(generic.ListView):
    model = User
    template_name = 'eCapture/profile_settings.html'


class StatusandLogView(generic.ListView):
    model = Attendance
    template_name = 'eCapture/status_log.html'
