from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns +=[
    url(r'clients/$', views.ClientsList.as_view(), name='client-list'),
    url(r'clients/(?P<pk>[-\w]+)/$', views.ClientDetail.as_view(), name='client-detail'),
    url(r'sites/$', views.SitesList.as_view(), name='site-list'),
    url(r'sites/(?P<pk>[-\w]+)/$', views.SiteDetail.as_view(), name='site-detail'),
    url(r'areas/$', views.AreasList.as_view(), name='area-list'),
    url(r'areas/(?P<pk>[-\w]+)/$', views.AreaDetail.as_view(), name='area-detail'),
    url(r'systems/$', views.SystemsList.as_view(), name='system-list'),
    url(r'systems/(?P<pk>[-\w]+)/$', views.SystemDetail.as_view(), name='system-detail'),
    url(r'components/$', views.ComponentsList.as_view(), name='component-list'),
    url(r'components/(?P<pk>[-\w]+)/$', views.ComponentDetail.as_view(), name='component-detail'),
    url(r'missions/$', views.MissionsList.as_view(), name='mission-list'),
    url(r'missions/(?P<pk>[-\w]+)/$', views.MissionDetail.as_view(), name='mission-detail'),
    url(r'tasks/$', views.TasksList.as_view(), name='task-list'),
    url(r'tasks/(?P<pk>[-\w]+)/$', views.TaskDetail.as_view(), name='task-detail'),
]
