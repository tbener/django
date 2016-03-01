'''
Created on Feb 22, 2016

@author: TBENER
'''

from django.db import models
from geo import Location

class Event(models.Model):
    date        = models.DateTimeField()
    location    = models.ForeignKey(Location, null=False)
    
    class Meta:
        app_label = "fma"
        

class Artist(models.Model):
    
    name        = models.CharField(max_length=50)
    events      = models.ManyToManyField(Event)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = "fma"
        


    
