from django.http import HttpResponse
from .models import Location, Event
from django.shortcuts import render

def index(request):
    context = {"events": Event.objects.all()}
    return render(request, "raven/index.html", context)

def detail(request, event_id):
    e = Event.objects.get(pk=event_id) 
    return HttpResponse(e.desc)

def locations(request):
    context = {"locations": Location.objects.all()}
    return render(request, "raven/locations.html", context)

def location_details(request, location_id):
    l = Location.objects.get(pk=location_id)
    return render(
        request, 
        "raven/location_details.html", 
        {
            "location": l, 
            "events": Event.objects.all().filter(location=l),
        }
    )

def date_details(request, event_id):
    print("Got here")
    d = Event.objects.get(pk=event_id).date.date()
    e = Event.objects.all().filter(date=d)
    print(d)
    print(e)
    context = {"events": Event.objects.all()}
    return render(
        request, 
        "raven/index.html", 
        {
            "date": d,
            "events": Event.objects.all().filter(date=d),
        }
    )