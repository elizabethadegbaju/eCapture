from django.contrib import admin
from django.urls import path

from . import views

app_name = 'eCapture'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('defaults/', views.defaults, name='defaults'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('profile/', views.history, name='profile'),
    path('users/add/', views.registration, name='registration'),
    path('users/<str:username>/', views.view_user, name='view_user'),
    path('dashboard/', views.admin, name='admin'),
]
