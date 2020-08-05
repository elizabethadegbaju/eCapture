from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from eCapture.models import Attendance, Department, Staff, Role, Event, \
    EventType


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
        return redirect('eCapture:profile')


def registration(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'registration/registration.html',
                      {'departments': departments, 'roles': roles})
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        dob = request.POST['dob']
        department_id = request.POST['department']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST['role']
        image = request.FILES['image']

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        new_staff = Staff.objects.create(user=new_user, dob=dob, role_id=role,
                                         department_id=department_id,
                                         image=image)
        new_staff.save()
        return redirect('eCapture:registration')


def admin(request):
    return render(request, 'eCapture/dashboard.html')


def index(request):
    return redirect('login')


def history(request):
    history = Attendance.objects.filter(user=request.user)
    return render(request, 'eCapture/status_log.html',
                  {'history': history})


def view_user(request, username):
    return None


def add_event(request):
    if request.method == 'GET':
        event_types = EventType.objects.all()
        return render(request, 'eCapture/add-event.html',
                      {'event_types': event_types})
    else:
        type_id = request.POST['type']
        location = request.POST['location']
        date = request.POST['date']
        event = Event.objects.create(location=location, date=date,
                                     type_id=type_id)
        event.save()
        return redirect('eCapture:admin')
