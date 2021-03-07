from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import School
# Create your views here.
def school(request):
    schoolData=serialize('geojson', School.objects.all())
    return HttpResponse(schoolData, content_type='geojson')

def home(response):
    return render(response, "main/home.html",{"name":"Home"})

def map(response):
    return render(response, "main/map.html",{"name":"Map"})
