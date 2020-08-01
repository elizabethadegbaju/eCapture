from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

from eCapture.models import Attendance


def defaults(request):
    defaults = Attendance.objects.filter(user=request.user, present=False,
                                         excused=False)
    return render(request, 'eCapture/defaults.html', {'defaults': defaults})


def profile_settings(request):
    if request.method == 'GET':
        return render(request, 'eCapture/profile_settings.html')
    elif request.method == 'POST':
        name = request.POST['name'].split(" ")
        password = request.POST['password']
        user = request.user
        user.set_password(password)
        user.first_name = name[0]
        user.last_name = name[1]
        user.save()
        update_session_auth_hash(request, user)
        return redirect('eCapture:history')


def registration(request):
    return render(request, 'registration/registration.html')


def admin(request):
    return render(request, 'eCapture/admin.html')


def index(request):
    return redirect('login')


def history(request):
    history = Attendance.objects.filter(user=request.user)
    return render(request, 'eCapture/status_log.html', {'history': history})
