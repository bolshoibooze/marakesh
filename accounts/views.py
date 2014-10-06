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


class IndexListView(ModelListView):
    model = About
    fields = (
    'main_photo','what_we_do',
    'who_we_are','how_it_works'
    )
    template_name = 'alt_index_list.html'
    mobile_template_name = 'm_index_list.html'
    
    
class FaqListView(ModelListView):
    model = Faq
    fields = ('qstn','answer')
    template_name = 'faq_list.html'
    mobile_template_name = 'm_faq_list.html'
    
class SuperContactView(CustomCreateView):
    model = Message
    fields = ('from_email','subject','msg')
    template_name = 'contact_form.html'
    mobile_template_name ='m_contact_form.html'
    success_url = reverse_lazy('thanks') 
    
    def form_valid(self, form):
        """
        msg = "{from_email} said: ".format(
        from_email=form.cleaned_data.get('from_email')
        )
        msg += "\n\n{0}".format(form.cleaned_data.get('msg'))
        """
        send_mail(
        subject = self.request.POST.get('subject', ''),
        from_email = self.request.POST.get('from_email', ''),
        #msg = self.request.POST.get('msg', '')
        
        )
        return super(SuperContactView, self).form_valid(form)
    
    
class ContactSuccess(MobileTemplateView):
    template_name = 'contact_success.html'
    mobile_template_name = 'm_contact_success.html'
    
     
    
    
class ContactView(MobileTemplateView):
    template_name = 'contact_us.html'  
    mobile_template_name =  'm_contact_us.html'
    
    
    
