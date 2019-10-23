from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns +=[
    path(r'clients', views.ClientAPIView.as_view(), name='client-list'),
    path(r'sites', views.SiteAPIView.as_view(), name='site-list'),
    path(r'areas', views.AreaAPIView.as_view(), name='area-list'),
    path(r'systems', views.SystemAPIView.as_view(), name='system-list'),
    path(r'components', views.ComponentAPIView.as_view(), name='component-list'),
    path(r'missions', views.MissionAPIView.as_view(), name='mission-list'),
    path(r'tasks', views.MissionAPIView.as_view(), name='task-list'),
]