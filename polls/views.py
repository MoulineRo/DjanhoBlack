from django.http import HttpResponse
from django.shortcuts import render
from .models import Teachers

def teachers(request):
    tech = [Teachers.objects.latest(10).name]
    return render(tech, 'index.html')

