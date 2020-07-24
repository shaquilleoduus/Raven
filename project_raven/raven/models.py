import datetime
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Event(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    desc = models.TextField()
    date = models.DateTimeField("event date")
    
    # add date here?

    def __str__(self):
        # return f"{self.desc[:20]}..."
        return self.desc
# class Date ??
