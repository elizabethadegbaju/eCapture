from django.shortcuts import render, redirect


def defaults(request):
    return render(request, 'eCapture/defaults.html')


def profile_settings(request):
    return render(request, 'eCapture/profile_settings.html')


def index(request):
    return redirect('login')


def history(request):
    return render(request, 'eCapture/status_log.html')
