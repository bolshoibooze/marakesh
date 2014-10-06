from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse,resolve
from .models import *
from .views import *
from accounts.models import *


urlpatterns = patterns('places.views',

    url(r'^destination/$', PlacesListView.as_view(), 
        name='destination_list'),
        
    url(r'^detail/(?P<pk>\d+)/$', PlaceDetailView.as_view(), 
        name='detail'),
        
    
)
