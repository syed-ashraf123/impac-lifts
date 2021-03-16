from django.shortcuts import render,HttpResponse
from datetime import datetime
from shaad.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method== "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('contact')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,phone=phone,message=message,date=datetime.today())
        contact.save()

    return render(request,"index.html")

def elevators(request):
    return render(request,"elevators.html")

def components(request):
    return render(request,"components.html")

def doors(request):
    return render(request,"doors.html")

def aboutus(request):
    return render(request,"aboutus.html")