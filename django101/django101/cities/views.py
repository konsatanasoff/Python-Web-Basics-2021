from django.http import HttpResponse
from django.shortcuts import render

from django101.cities.models import Person


def index(req):
    context = {
        'name': 'Johnny',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def list_cities(request):
    context = {
        'cities': [
            'Barcelona',
            'Madrid',
            'Paris',
            'Sofia',
        ]
    }
    return render(request, 'cities.html', context)