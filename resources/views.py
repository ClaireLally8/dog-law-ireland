from django.shortcuts import render

from .models import Resource

def resources(request):
    resources = Resource.objects.all()
    context = {
        'resources':resources
    }
    return render(request, 'resources/resources.html', context)