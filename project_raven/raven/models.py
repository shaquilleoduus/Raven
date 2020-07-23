import datetime
from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

class Event(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    event_desc = models.CharField(max_length=200)
    event_date = models.DateTimeField("event date")
    
    # add date here?

    def __str__(self):
        return self.event_desc

# class Date ??
