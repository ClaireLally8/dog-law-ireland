from django.shortcuts import render

from .models import Resource

def resources(request):
    resources = Resource.objects.all()
    context = {
        'resources':resources
    }
    return render(request, 'resources/resources.html', context)

def resource_detail(request, slug):
    resource = get_object_or_404(resource, slug=slug)
    return render(request, 'resources/resource_detail', {'resource': resource})
