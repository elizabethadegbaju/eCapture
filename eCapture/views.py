from django.shortcuts import render, redirect

from eCapture.models import Attendance


def defaults(request):
    defaults = Attendance.objects.filter(user=request.user, present=False,
                                         excused=False)
    return render(request, 'eCapture/defaults.html', {'defaults': defaults})


def profile_settings(request):
    return render(request, 'eCapture/profile_settings.html')

def registration(request):
    return render(request, 'registration/registration.html')


def admin(request):
    return render(request, 'eCapture/admin.html')


def index(request):
    return redirect('login')


def history(request):
    history = Attendance.objects.filter(user=request.user)
    return render(request, 'eCapture/status_log.html', {'history': history})
