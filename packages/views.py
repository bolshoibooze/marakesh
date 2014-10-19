from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy,resolve

from marakesh.settings import *
from ua_detector.views import *
from ua_detector.generic_views import *
from ua_detector.model_views import *
from .models import *


class PackageListView(ModelListView):
    model = OtherPackage
    fields = (
    'name','overview'
    )
    mobile_template_name ='m_package_list.html'
    template_name = 'package_list.html'
    
class PackageDetailView(ModelDetailView):
    model = OtherPackage
    mobile_template_name ='m_package_detail.html'
    template_name = 'package_detail.html'
    
    
class RegistrationView(CustomCreateView):
    fields = (
    'full_name','gender','phone_number',
    'id_number'
    )
    model = Participant
    template_name = 'registration_form.html'
    mobile_template_name = 'm_registration_form.html'
    success_url = reverse_lazy('reg_success')


class RegistrationSuccess(MobileTemplateView):
    mobile_template_name = 'm_reg_success.html'
    template_name = 'reg_success.html'


