from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Client, Site, Area, System, Component, Mission, Task
from .serializers import ClientSerializer, SiteSerializer, AreaSerializer, SystemSerializer, ComponentSerializer, MissionSerializer, TaskSerializer

def index(request):
    return HttpResponse("<h1>Hello, world. I'm gonna be a CMMS one day</h1>")

#RESTing a bit below
class ClientsList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class SitesList(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class AreasList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    filterset_fields = ['site_id']

class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class SystemsList(generics.ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    filterset_fields = ['area_id', 'id']

class SystemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

class ComponentsList(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    filterset_fields = ['system_id', 'id']

class ComponentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class MissionsList(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    filterset_fields = ['component_id', 'id']

class MissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class TasksList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = MissionSerializer
    filterset_fields = ['mission_id']

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = MissionSerializer
