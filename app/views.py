from django.shortcuts import render

from .models import Animals


def home(request):
    animals = Animals.objects.all()

    context = {
        'animals': animals
    }

    return render(request, 'index.html', context)


def not_found(request):
    return render(request, '404.html')
