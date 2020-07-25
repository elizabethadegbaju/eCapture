from django.shortcuts import render, redirect
from django.views import generic
from .models import Attendance, User


class DefaultsView(generic.ListView):
    model = Attendance
    template_name = 'eCapture/defaults.html'


class ProfileSettingsView(generic.ListView):
    model = User
    template_name = 'eCapture/profile_settings.html'


class StatusandLogView(generic.ListView):
    model = Attendance
    template_name = 'eCapture/status_log.html'


def index(request):
    return redirect('login')


def history(request):
    return render(request, 'eCapture/status_log.html')
