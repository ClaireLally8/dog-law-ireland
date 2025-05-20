from django.shortcuts import render
from events.models import Event

# Create your views here.
def index(request):
    featured = Event.objects.filter(featured=True).first()

    context = {
        'featured': featured,
    }

    return render(request,'main/index.html', context)
