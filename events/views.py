from django.shortcuts import render, get_object_or_404
from .models import Event

def events(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})

