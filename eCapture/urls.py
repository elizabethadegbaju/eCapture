from django.urls import path
from django.contrib import admin
from . import views

app_name = 'eCapture'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('defaults/', views.defaults, name='defaults'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('status_logs/', views.history, name='history'),

]
