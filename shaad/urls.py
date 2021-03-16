from django.contrib import admin
from django.urls import path
from shaad import views

urlpatterns = [
    path('index', views.index,name="index"),
    path('', views.index,name="index"),
    path('elevators', views.elevators,name="elevators"),
    path('components', views.components,name="components"),
    path('doors', views.doors,name="doors"),
    path('aboutus', views.aboutus,name="aboutus")
    ]
