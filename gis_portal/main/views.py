from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(response):
    return render(response, "main/home.html",{"name":"Home"})