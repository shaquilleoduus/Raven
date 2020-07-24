from django.http import HttpResponse
from .models import Location, Event
from django.shortcuts import render
import datetime

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
            "events": Event.objects.all().filter(date__year=d.year).filter(date__month=d.month).filter(date__day=d.day)
            # "events": Event.objects.all().filter(date__startswith=d),
        }
    )

def events_by_year(request, event_year):
    return render(
        request,
        "raven/index.html",
        {
            "date": datetime.date(event_year, 1, 1),
            "events": Event.objects.filter(date__year=event_year),
        }
    )

def events_by_year_month(request, event_year, event_month):
    return render(
        request,
        "raven/index.html",
        {
            "date": datetime.date(event_year, event_month, 1),
            "events": Event.objects.filter(date__year=event_year).filter(date__month=event_month),
        }
    )

def events_by_year_month_day(request, event_year, event_month, event_day):
    return render(
        request,
        "raven/index.html",
        {
            "date": datetime.date(event_year, event_month, event_day),
            "events": Event.objects.filter(date__year=event_year).filter(date__month=event_month).filter(date__day=event_day),
        }
    )