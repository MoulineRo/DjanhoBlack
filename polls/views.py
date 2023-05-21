from django.http import HttpResponse
from faker import Faker

from .models import Teachers


def index(request):
    return HttpResponse("generate_teachers")


def teachers(requsts):
    fake = Faker()
    fake.name()
    for _ in range(100):
        Teachers.objects.create(name=fake.name())
    tech = Teachers.objects.in_bulk()
    teachers1 = []
    for tec in tech:
        teachers1.append(tech[tec].name)
    return HttpResponse(teachers1[-100:])
