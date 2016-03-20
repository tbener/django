'''
Created on Feb 22, 2016

@author: TBENER
'''

from django.contrib import admin
from .models import *

# admin.site.register(User)
admin.site.register(AlertDefinition)
admin.site.register(Event)
admin.site.register(Artist)

