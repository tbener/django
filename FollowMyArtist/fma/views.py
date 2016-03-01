from django.shortcuts import render
from FollowMyArtist import settings
from .forms import AlertForm, LocationForm
from django.http.response import HttpResponse
from django.utils import simplejson
from .models.alerts import AlertDefinition
from fma.models.geo import Location
from django.contrib.auth.models import User


def home(request):
    form_alert = AlertForm()
    form_location = LocationForm()
    return render(request, 'main.html', { 'GOOGLE_KEY': settings.GOOGLE_KEY, 'form_alert': form_alert, 'form_location': form_location})

def add_alert(request):
    if request.method == 'POST':
        form = AlertForm(request.POST)
        data = form.data
         
        location = Location()
        location.lat = data.get("lat", 0)
        location.lng = data.get("lng", 0)
        location.name = data.get("location", "(Custom)")
        location.save()
          
        alert = AlertDefinition()
        alert.user = User.objects.get(pk=1)
        alert.name = '{0}_{1}'.format(alert.user.username, AlertDefinition.objects.count() + 1)
        alert.location = location
        alert.distance = data.get("distance", 0)
        alert.save()
 
        print('Saved: {0}'.format(alert.description()))
        return HttpResponse(
            simplejson.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )