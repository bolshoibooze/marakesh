from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse,resolve
from .models import *
from .views import *
from accounts.models import *


urlpatterns = patterns('bookings.views',

    
    url(r'^bookings/$', BookingView.as_view(), 
        name='bookings'),
        
    url(r'^booking_success/$', BookingSuccess.as_view(), 
        name='booking_success'),
    
)
