import re 
import math
from datetime import *
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from marakesh.settings import *
from .date_widget import *
from .models import *

#source:<http://stackoverflow.com/questions/9936434/django-forms-datefield>
class DateFieldValidator(forms.DateField):
    def validate(self, value):
        if not re.match(r'[0-9]{2}-[0-9]{2}-[0-9]{4}', value):
            raise forms.ValidationError(
            'Sorry,wrong date format:enter date-month-Year'
            )


class BookingForm(forms.ModelForm):
    special_request = forms.CharField(
      max_length=250,label='Special Request',
      widget=forms.Textarea(attrs={'rows':1,'cols':17}),
      
    )
    checkin_date = forms.DateField(
      initial='day-month-Year',
      input_formats=['%d-%m-%Y',], 
    label='Checkin Date'
    )
    class Meta(object):
        model = BookingMaster
        exclude = (
        'deposit','amount','transaction_id',
        'children','under_5','date'
        )
        
   
    
          
       
