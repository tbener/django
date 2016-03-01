'''
Created on Feb 29, 2016

@author: TBENER
'''

from django import forms
from fma import widgets

class CharField(forms.CharField):
    widget = widgets.TextInput
    
class FloatField(forms.FloatField):
    widget = widgets.TextInput