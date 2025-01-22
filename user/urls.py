from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path("home/", views.home, name='home'),   
    path("login/", views.login1, name='login'),   
    path("logout/", views.logout1, name='logout'),   
    path("signup/", views.signup, name='signup'),
    path("profile/", views.profileManage, name='profile'),
    # path("", views.startUpRedirect, name='startup')   
]