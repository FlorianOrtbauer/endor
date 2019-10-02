from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world. I'm gonna be a CMMS one day</h1>")
