from django.shortcuts import render


def index(req):
    context = {
        'name': 'Johnny',
    }
    return render(req, 'index.html', context)