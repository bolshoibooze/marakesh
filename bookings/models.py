from __future__ import(
absolute_import, unicode_literals
) 


import re
import math 
import datetime
from django.db import models
from django.db.models import *
from django.contrib import auth
from django.contrib.auth.models import *
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode
from tinymce.models import HTMLField
from marakesh.settings import *
from places.models import *




          
class BookingMaster(models.Model):
    destination = models.ForeignKey(
       Place,related_name='+',
       verbose_name='Destination'
    )
    full_name = models.CharField(
       max_length=100,null=True,
       blank=True
    )
    phone_number = models.CharField(
       max_length=50,
       verbose_name='Phone Number',
       null=True,blank=True
    )
    id_number = models.CharField(
       max_length=50,null=True,
       blank=True
    )
    checkin_date = models.DateField(
       auto_now_add=False
    )
    nights = models.CharField(
       max_length=50,default='3'
    )
    checkout_date = models.DateField(
       auto_now_add=False,
       null=True,blank=True
    )
    special_request = HTMLField(
       max_length=450,
       verbose_name='Special Request',
       null=True,blank=True
    )
    deposit = models.IntegerField(
       default=0,null=True,blank=True
    )
    transaction_id = models.CharField(
       max_length=128,
       null=True,blank=True
    )
    adults = models.CharField(
       max_length=50,default='2',
       null=True,blank=True
    )
    children = models.CharField(
       max_length=50,default='0',
       null=True,blank=True
    )
    under_5 = models.CharField(
       max_length=50,default='0',
       null=True,blank=True
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'Booking Manager'
        ordering = ['date']
        verbose_name_plural = 'Bookings Manager'
        
        
    def __unicode__(self):
        return self.full_name
        
    def set_to_date(self):
        objs = BookingMaster.objects.filter(
        Q(checkin_date=checkin_date)& Q(nights=nights)&
        Q(checkout_date=checkout_date)
        )
        for obj in objs:
            pass
            
    @property
    def update_booking(self):
        objs = BookingMaster.objects.filter(
        Q(destination__is_available=destination__is_available)&
        Q(destination=destination)& Q(date=date)
        )
        for obj in objs:
            if obj.date == datetime.datetime.today():
               place = obj.destination
               update = BookingMaster.objects.update(
               destination=place,destination__is_available=False
               
               )
               return update
            
        
        
          
    def save(self,*args,**kwargs):
        super(BookingMaster,self).save(*args,**kwargs) 
        
        
        
        
        
        
