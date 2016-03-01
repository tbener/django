'''
Created on Feb 22, 2016

@author: TBENER
'''
from django.utils.translation import ugettext as _
from django.db import models

class Location(models.Model):
    place        = models.CharField(max_length=100)
    lat         = models.FloatField(_('Latitude'), blank=True, null=True)
    lng         = models.FloatField(_('Longitude'), blank=True, null=True)
    
    def __unicode__(self):
        return self.place or '({0}, {1})'.format(self.lat, self.lng)
    
    class Meta:
        app_label = "fma"