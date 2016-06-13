"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from fma import views

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    
    url(r'^$', views.user_main_view, name='main'),
    url(r'^test/', views.test),
    url(r'^add-alert/', views.add_alert),
    url(r'^admin/', admin.site.urls),
    url(r'^get_artist/', views.get_artist),
    
    url(r'^mypage/$', views.user_main_view, name='user_main'),
    
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.artist, name='artist'),
    
    url(r'^(?P<artist_slug>[a-z]+)/$', views.events, name='events'),
    
    url(r'^complete/google-oauth2/$', views.user_main_view, name='user_main'),
    
    
    
    
    
]
