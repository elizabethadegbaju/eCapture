from django.urls import path
from django.contrib import admin
from . import views

app_name = 'eCapture'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('defaults/', views.DefaultsView.as_view(), name='defaults'),
    path('profile_settings/', views.ProfileSettingsView.as_view(), name='profile_settings'),
    path('status_logs/', views.StatusandLogView.as_view(), name='status_logs'),


]
