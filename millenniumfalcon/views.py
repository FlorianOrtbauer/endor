from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Client, Site, Area, System, Component, Mission, Task, Supplier
from .serializers import ClientSerializer, SiteSerializer, AreaSerializer, SystemSerializer, ComponentSerializer, MissionSerializer, TaskSerializer, SupplierSerializer

def index(request):
    return HttpResponse(
        "<h1>CMMS Backend [REST API]</h1>"+
        "<p>Python Django based backend for Campus02 Webentwicklung project.</p>"+
        "<p>Direct ressource access provides possibility to modify data in the database via the backend application.</p>"+
        "<p>URL:<i>url</i>/millenniumfalcon/<i>ressource</i> </p>"+
        "<h2>Available ressources:</h2>"+
        "<h3>/clients</h3>"+
        "<p>Backend filter option: none</p>"+
        "<h3>/sites</h3>"+
        "<p>Backend filter option: client_id</p>"+
        "<h3>/areas</h3>"+
        "<p>Backend filter option: site_id</p>"+
        "<h3>/systems</h3>"+
        "<p>Backend filter option: area_id, id</p>"+
        "<h3>/components</h3>"+
        "<p>Backend filter option: system_id, id</p>"+
        "<h3>/missions</h3>"+
        "<p>Backend filter option: component_id, id</p>"+
        "<h3>/tasks</h3>"+
        "<p>Backend filter option: task_id, id</p>"+
        "<h3>/suppliers</h3>"+
        "<p>Backend filter option: none</p>"
        )

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
    filterset_fields = ['client_id']

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
    serializer_class = TaskSerializer
    filterset_fields = ['mission_id']

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    #filterset_fields = ['client_id']

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
