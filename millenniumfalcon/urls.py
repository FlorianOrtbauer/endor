from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns +=[
    url(r'clients/$', views.ClientsList.as_view(), name='client-list'),
    url(r'sites/$', views.SitesList.as_view(), name='site-list'),
    url(r'areas/$', views.AreasList.as_view(), name='area-list'),
    url(r'systems/$', views.SystemsList.as_view(), name='system-list'),
    url(r'systems/(?P<pk>)', views.SystemDetail.as_view(), name='system-list'),
    url(r'components/$', views.ComponentsList.as_view(), name='component-list'),
    url(r'components/(?P<pk>)', views.ComponentDetail.as_view(), name='component-list'),
    url(r'missions/$', views.MissionsList.as_view(), name='mission-list'),
    url(r'missions/(?P<pk>)', views.MissionDetail.as_view(), name='mission-list'),
    url(r'tasks/$', views.TasksList.as_view(), name='task-list'),
]