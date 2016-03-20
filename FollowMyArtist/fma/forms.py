'''
Created on Feb 26, 2016

@author: TBENER
'''
from django import forms

from .models.alerts import AlertDefinition, ALERT_TYPES
from .models.geo import Location
from fma import fields as fma
from django.forms.models import BaseInlineFormSet

class LocationForm(forms.ModelForm):
    
    class Meta:
        model = Location
        fields = ['place', 'lat', 'lng']
        widgets = {'place' : forms.TextInput(attrs = {'class': 'form-control'}),
                   'lat' : forms.HiddenInput(),
                   'lng' : forms.HiddenInput(),}

class AlertForm(forms.ModelForm):
    
    class Meta:
        model = AlertDefinition
        fields = ['name', 'alert_type', 'distance']
        widgets = {'distance' : forms.TextInput(attrs = {'class': 'form-control'})}
        

class AlertForm2(forms.ModelForm):
    place       = fma.CharField(max_length=100, required=False)
    lat         = forms.FloatField(widget=forms.HiddenInput())
    lng         = forms.FloatField(widget=forms.HiddenInput())
    
    class Meta:
        model = AlertDefinition
        fields = ['place', 'lat', 'lng', 'alert_type', 'distance']
        widgets = {'distance' : forms.TextInput(attrs = {'class': 'form-control'})}

class AlertForm1(forms.Form):
    place       = fma.CharField(max_length=100, required=False)
    lat         = forms.FloatField(widget=forms.HiddenInput())
    lng         = forms.FloatField(widget=forms.HiddenInput())
    alert_type  = fma.CharField(label='Select by', max_length=20, initial=ALERT_TYPES[0][0], widget=forms.Select(choices=ALERT_TYPES))
    distance    = fma.FloatField(initial=40000)

    class Meta:
        fields = ['place', 'lat', 'lng', 'alert_type', 'distance']
    
