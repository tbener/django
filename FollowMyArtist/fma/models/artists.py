'''
Created on Mar 6, 2016

@author: TBENER
'''

from django.db import models
from django.utils.translation import ungettext
from .database_storage import DatabaseStorage

DBS_OPTIONS = {
    'table':'fma_files', 
    'base_url':'/fma/files/'}

class Artist(models.Model):
    
    name        = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def short_description(self):
        return '{0} {1}'.format(self.alertdefinition_set.count(), ungettext('alert', 'alerts', self.alertdefinition_set.count()))
    
    class Meta:
        app_label = "fma"