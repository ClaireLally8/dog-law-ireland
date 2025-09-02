from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Resource

def resources(request):
    resources_qs = (
        Resource.objects
        .order_by("position", "-uploaded_at")  # explicit & stable
        .prefetch_related("images")
    )
    paginator = Paginator(resources_qs, 12)
    page_number = request.GET.get('page') or 1
    page_obj = paginator.get_page(page_number)
    context = {
        'resources': page_obj
    }
    return render(request, 'resources/resources.html', context)

def resource_detail(request, slug):
    resource = get_object_or_404(Resource, slug=slug)
    return render(request, 'resources/resource_detail.html', {'resource': resource})
