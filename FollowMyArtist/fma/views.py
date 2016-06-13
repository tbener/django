from django.shortcuts import render, get_object_or_404, redirect
from FollowMyArtist import settings
from .forms import AlertForm, LocationForm
from django.http.response import HttpResponse
import json 
from .models import *
from django.forms.models import inlineformset_factory, modelform_factory
# from fma.models.users import FmaUser as User

# from django.contrib.auth import get_user_model
# User = get_user_model()

def user_main_view(request):
    user = request.user
    if user and not user.is_anonymous():
        alerts = user.alertdefinition_set.all()
        artists = Artist.objects.filter(alertdefinition__in=alerts).distinct()
    else:
        alerts = None
        artists = None
    form_artist = modelform_factory(Artist, fields=['name'])
    form_alert = AlertForm()
    form_location = LocationForm()
    return render(request, 'user_main.html', { 'GOOGLE_KEY': settings.GOOGLE_KEY, 'request': request, 'user': request.user, 
                                              'artists': artists, 'alerts': alerts, 'form_alert': form_alert, 
                                              'form_location': form_location, 'form_artist': form_artist})

def add_alert(request):
    user = request.user
    
    form_artist = modelform_factory(Artist, fields=['name'])
    form_alert = AlertForm()
    form_location = LocationForm()
    return render(request, 'add_alert.html', { 'GOOGLE_KEY': settings.GOOGLE_KEY, 'request': request, 'user': user, 
                                              'form_alert': form_alert, 
                                              'form_location': form_location, 'form_artist': form_artist})


def home(request):
    form_loc = LocationForm()
    form_alert = AlertForm()
    #inline_ = inlineformset_factory(Location, AlertDefinition, extra=1, fields=['name', 'artists', 'alert_type', 'distance'])
    #form_location = LocationFormSet()
    return render(request, 'main.html', { 'GOOGLE_KEY': settings.GOOGLE_KEY, 'request': request, 'user': request.user, 'form_alert': form_alert, 'form_location': form_loc})

def test(request):
    form_loc = LocationForm()
    form_alert = AlertForm()
    
    return render(request, 'main_test.html', { 'GOOGLE_KEY': settings.GOOGLE_KEY, 'request': request, 'user': request.user, 'form_alert': form_alert, 'form_location': form_loc})


def get_artist(request):
    if request.is_ajax():
        artists = []
        artist_json = {}
        artist_name = request.POST.get('artist_name')
        a = Artist.objects.filter(name__icontains = artist_name).first()
        if a:
            data = {'name': a.name, 'id': a.pk}
            
        
        print(data)
            
        data = json.dumps(data)
    else:
        data = 'fail'    
    
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


    

def add_alert_old(request):
    if request.method == 'POST':
        data = request.POST
         
        location = Location()
        location.lat = data.get("lat", 0)
        location.lng = data.get("lng", 0)
        location.place = data.get("place", "(Custom)")
        location.save()
          
        alert = AlertDefinition()
        alert.user = User.objects.get(pk=1)
        alert.name = '{0}_{1}'.format(alert.user.username, AlertDefinition.objects.count() + 1)
        alert.distance = data.get("distance", 0)
        alert.save()
        
        alert.location.add(location)
        alert.artists.add(1)
        
 
        print('Saved: {0}'.format(alert.description()))
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
        
def events(request, artist_slug):
    artist = Artist.objects.filter(slug = artist_slug).first()
    if artist:
        html = artist.name
    else:
        html = 'No artist found! (%s)' % artist_slug
        
    return HttpResponse(html)


def artist(request, artist_id):
    artist = Artist.objects.filter(pk = artist_id).first()
    if artist:
        html = artist.name
    else:
        html = 'No artist found! (%s)' % artist_id
        
    return HttpResponse(html)

