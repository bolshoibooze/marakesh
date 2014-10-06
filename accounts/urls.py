from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse,resolve
from .models import *
from .views import *
from accounts.models import *


urlpatterns = patterns('accounts.views',

    url(r'^index/$', IndexListView.as_view(), 
        name='site_index'),
        
    url(r'^faqs/$', FaqListView.as_view(), 
        name='create_sub'),
        
    url(r'^contacts/$',ContactView.as_view(),
        name='contact_us'),
        
    url(r'^thanks',ContactSuccess.as_view(),
        name='thanks'),
           
    url(r'^faqs/$',FaqListView.as_view(),
        name='faqs'),
        
)
