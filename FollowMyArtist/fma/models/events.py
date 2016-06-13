'''
Created on Feb 22, 2016

@author: TBENER
'''

from django.db import models
from .geo import Location
from .artists import Artist

class Event(Location):
    name        = models.CharField(max_length=100)
    date        = models.DateTimeField()
    artists     = models.ManyToManyField(Artist)
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "fma"
        

        


    
