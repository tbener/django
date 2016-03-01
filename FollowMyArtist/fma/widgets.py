'''
Created on Feb 29, 2016

@author: TBENER
'''

from django import forms

class TextInput(forms.TextInput):
    def __init__(self, attrs={}):
        attrs['class'] = 'form-control'
        super(TextInput, self).__init__(attrs)