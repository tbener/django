'''
Created on Feb 22, 2016

@author: TBENER
'''

from django.db import models
from django.utils.encoding import force_text
from django.contrib.auth.models import User

from .events import Event, Artist
# from .users import FmaUser as User
from .geo import Location



ALERT_TYPES = (
        ('RADIUS', 'Radius'),
        ('LON_EAST', 'Longitude - East'),
        ('LON_WEST', 'Longitude - West'),
        ('LAT_NORTH', 'Latitude - North'),
        ('LAT_SOUTH', 'Latitude - South'),
        ('REGION', 'Region'),
        ('LOCATION', 'Specific Location'),
               )


class AlertDefinition(Location):
    user            = models.ForeignKey(User, null=False)
    name            = models.CharField(max_length=50)
    artists         = models.ManyToManyField(Artist)
    alert_type      = models.CharField(verbose_name='Select by', max_length=20, choices=ALERT_TYPES, default=ALERT_TYPES[0][0])
    distance        = models.PositiveIntegerField(verbose_name='Radius', default=20000)
    days_list       = models.CharField(max_length=100, null=True, help_text='How many days before the event takes place you will be notified')
    alert_time      = models.TimeField(verbose_name='Notification time', null=True, help_text='The time in the day that you would like to receive the notification (optional).')
    
    def __str__(self):
        return self.name
    
    def description(self):
        return 'Alert: {0}, At: {1}, By {2} (radius {3}m)'.format(self.name, self.location.name, self.alert_type, self.distance)
    
    def short_description(self):
        return ', '.join(force_text(a) for a in self.artists.all())
    
    class Meta:
        app_label = "fma"

class AlertSent(models.Model):
    event       = models.ForeignKey(Event)
    user        = models.ForeignKey(User)
    date_time   = models.DateTimeField()
    
    class Meta:
        app_label = "fma"
    
    
class AlertToSend(models.Model):
    event       = models.ForeignKey(Event)
    user        = models.ForeignKey(User)
    days_requested = models.PositiveIntegerField()
    
    class Meta:
        app_label = "fma"