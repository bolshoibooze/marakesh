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
from bookings.forms import BookingForm

class BookingView(CustomCreateView):
    model = BookingMaster
    form_class = BookingForm
    """
    fields = (
    'destination','full_name','phone_number',
    'id_number','checkin_date','checkout_date','adults',
    'special_request'
    )
    """
    template_name = 'booking_form.html'
    mobile_template_name = 'm_booking_form.html'
    success_url = reverse_lazy('bookings')
    
 
class BookingSuccess(MobileTemplateView):
    template_name = 'success.html'
    mobile_template_name = 'm_success.html'

    
    
    
    
