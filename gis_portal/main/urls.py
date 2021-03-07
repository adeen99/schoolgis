from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("map/", views.map, name="map"),
    path("schooldata", views.school, name="schooldata"),
]
