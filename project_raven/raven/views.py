from django.http import HttpResponse
from .models import Location, Event
from django.shortcuts import render

def index(request):
    context = {"events": Event.objects.all()}
    return render(request, "raven/index.html", context)

def detail(request, event_id):
    e = Event.objects.get(pk=event_id) 
    return HttpResponse(e.event_desc)