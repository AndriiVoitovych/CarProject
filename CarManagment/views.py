from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Car

def index(request):
    template = loader.get_template('car/index.html')
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return HttpResponse(template.render(context, request))

def addCar(request):
    return HttpResponse(request, 'add_car.html') 
