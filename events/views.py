from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Event

# events/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Event

def events(request):
    # Pick the top Featured event by your manual order, then newest as tiebreaker
    featured = (
        Event.objects
        .filter(featured=True)
        .order_by("order", "-uploaded_at")
        .prefetch_related("images")
        .first()
    )

    # Non-featured list, ordered by your manual order then newest
    base_qs = (
        Event.objects
        .filter(featured=False)  # keeps featured out of the list
        .order_by("order", "-uploaded_at")  # explicit & stable
        .prefetch_related("images")
    )

    # (Optional) If you want to exclude the featured item even if someone double-featured by mistake:
    if featured:
        base_qs = base_qs.exclude(pk=featured.pk)

    paginator = Paginator(base_qs, 12)
    page_obj = paginator.get_page(request.GET.get("page") or 1)

    context = {
        "featured": featured if page_obj.number == 1 else None,  # show hero only on page 1
        "events": page_obj,
    }
    return render(request, "events/events.html", context)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'events/event_detail.html', {'event': event})


