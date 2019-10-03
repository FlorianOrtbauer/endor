from rest_framework import serializers
from .models import Client, Site, Area, System, Component, Mission, ExecTask

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = "__all__"

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = "__all__"

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = "__all__"

class ExecTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecTask
        fields = "__all__"
