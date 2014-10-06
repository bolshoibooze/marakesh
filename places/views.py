from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext


from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy,resolve

from marakesh.settings import *
from ua_detector.views import *
from ua_detector.generic_views import *
from ua_detector.model_views import *
from .models import *
from .forms import *


class PlacesListView(ModelListView):
    model = Place
    fields = (
    'name','location','main_photo',
    'description','is_available'
    )
    template_name = 'places_list.html'
    mobile_template_name = 'm_places_list.html' 
    

class PlaceDetailView(ModelDetailView):
    model = Place
    template_name = 'place_detail.html'
    mobile_template_name = 'm_place_detail.html' 
    
    

    
    
class DetailView(MobileDetailView):
    template_name = None
    mobile_template_name = None
    context_object_name = None
    queryset = None

    def get_context_data(self,**kwargs):
        context=super(DetailView,self).get_context_data(**kwargs)
        return context

    
    

class TermsListView(ModelListView):
    model = Terms
    fields = ('title','post',)
    template_name = 'terms_list.html'
    mobile_template_name = 'm_terms_list.html' 
