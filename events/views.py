from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Event

def events(request):
    featured = Event.objects.filter(featured=True).first()
    events_qs = Event.objects.exclude(pk=featured.pk).order_by('-uploaded_at') if featured else Event.objects.all().order_by('-uploaded_at')
    paginator = Paginator(events_qs, 12)
    page_number = request.GET.get('page') or 1
    page_obj = paginator.get_page(page_number)
    
    context = {
        'featured': featured,
        'events': page_obj,
    }
    return render(request, 'events/events.html', context)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'events/event_detail.html', {'event': event})


