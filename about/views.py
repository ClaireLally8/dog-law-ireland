from django.shortcuts import render
from .models import About
from resources.models import Resource

# Create your views here.
def about(request):
    about = About.objects.all()
    xlreview = Resource.objects.get(slug='Judicial-Review')
    context = {
        'about':about,
        'xlreview': xlreview,
    }
    return render(request,'about/about.html', context)
