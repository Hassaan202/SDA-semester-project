from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ai/', views.aiPage, name='ai'),
    path('resources/', views.resourcesLib, name='resources'),
    path('sharing/', views.resourceSharing, name='sharing'),
    path('forum/', views.discussion_forum, name='forum'),
]