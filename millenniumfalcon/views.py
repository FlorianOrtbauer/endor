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
class ClientAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class SiteAPIView(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class AreaAPIView(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    filterset_fields = ['site_id']

class SystemAPIView(generics.ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    filterset_fields = ['area_id', 'id']

class ComponentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    filterset_fields = ['system_id', 'id']

class MissionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    filterset_fields = ['component_id', 'id']

class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = MissionSerializer
    filterset_fields = ['mission_id']
