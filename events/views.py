from django.shortcuts import render, get_object_or_404
from .models import Event

def events(request):
    featured = Event.objects.filter(featured=True).first()
    events = Event.objects.exclude(pk=featured.pk) if featured else Event.objects.all()
    
    context = {
        'featured': featured,
        'events': events,
    }
    return render(request, 'events/events.html', context)

