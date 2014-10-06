from __future__ import absolute_import

from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

from yawdadmin import admin_site
admin_site._registry.update(admin.site._registry)

urlpatterns = patterns('',
    
    url(r'^accounts/', include('accounts.urls')),
    
    url(r'^places/', include('places.urls')),
    
    url(r'^bookings/', include('bookings.urls')),
    
    url(r'^ua_detector/',include('ua_detector.urls')),
    
    url(r'^tinymce/', include('tinymce.urls')),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
