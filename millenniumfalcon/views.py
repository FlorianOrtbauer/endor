from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

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

class SystemAPIView(generics.ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

class ComponentAPIView(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class MissionAPIView(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = MissionSerializer

