from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse,resolve
from .models import *
from .views import *



urlpatterns = patterns('packages.views',

    url(r'^list/$', PackageListView.as_view(), 
        name='package_list'),
        
    url(r'^details/(?P<pk>\d+)/$', PackageDetailView.as_view(), 
        name='package_details'),
        
    url(r'^signup/$',RegistrationView.as_view(),
        name='signup'),
        
    url(r'^reg_success/$',RegistrationSuccess.as_view(),
        name='reg_success'),
        
        
        
    
)
