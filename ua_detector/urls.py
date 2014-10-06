
from django.conf.urls.defaults import patterns, url

from ua_detector import views

urlpatterns = patterns('',
    url(r'full-site/$', views.FullSiteView.as_view(), name="full_site"),
)
