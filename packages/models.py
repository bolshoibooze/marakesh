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

#from places.models import Place




       
class Costing(models.Model):
    place = models.CharField(
       max_length=50,db_index=True,
       verbose_name='Name of Place'
    )
    category = models.CharField(
        max_length=100,
        choices = settings.CATEGORIES,
        help_text='e.g,Full Board',
        verbose_name='Category'
    )
    room_type = models.CharField(
       max_length=50,
       verbose_name='Room Type',
       help_text='e.g,Double,cottage,etc'
    )
    season = models.CharField(
       max_length=100,
       choices=settings.TYPES,
       verbose_name='Season'
    )
    start_date = models.DateField(
       auto_now_add=False,
       verbose_name='Start Date',
       help_text='Season start date'
    )
    end_date = models.DateField(
       auto_now_add=False,
       verbose_name='End Date',
       help_text='Season end date'
    )
    cost = models.IntegerField(
       verbose_name='Cost Per Night',
       help_text='Per person'
    )
    class Meta(object):
        db_table = 'Season Costing'
        verbose_name_plural = 'Season Costing'
        #ordering = ['cost','place',]
        
    def __unicode__(self):
        return smart_unicode(self.place)
        
     
        
    @property 
    def set_season(self):
        objs = Costing.objects.all()
        today = datetime.datetime.today()
        for obj in objs:
            #Booking must be 14 days in advance
            adjusted_time = datetime.timedelta(days=14)
            start_date = obj.start_date + time
            end_date = obj.end_date + time
            adjusted_date = today + time
            current_ssn = obj.season
            #lies between two dates
            if start_date >= adjusted_date <= end_date:
               #self.season = current_ssn
               #models.Model.save(self)
               #or
               ssn = Costing.objects.update(season=current_ssn)
               return ssn
        
           
    def save(self,*args,**kwargs):
        super(Costing,self).save(*args,**kwargs)


class Package(models.Model):
    price = models.ForeignKey(
       Costing,db_index=True,
       verbose_name='Name of Place',
       related_name='+'
    )
    category = models.CharField(
       max_length=100,
       choices=settings.CATEGORY,
       default=settings.CATEGORY[0][0]
    )
    nights = models.IntegerField(
       default=3
    )
    description = HTMLField(
       max_length=450,
       verbose_name='Package'
    )
    deposit = models.IntegerField(
       default=0,verbose_name='Deposit'
    )
    total_cost = models.IntegerField(
       verbose_name='Cost'
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    user = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       related_name='+'
    )
    class Meta(object):
        db_table = 'Package Details'
        ordering = ['price','total_cost',]
        verbose_name_plural='Package Details'
        
    def __unicode__(self):
        return smart_unicode(self.price)
        
    
            
    def set_total_cost(self):
        objs = Package.objects.filter(
        Q(price__cost=price__cost)&
        Q(price__place=price__place)&
        Q(nights=nights)
        )
        pass
        
    @property
    def set_deposit(self):
        objs = Package.objects.filter(
        Q(price__place=price__place)&
        Q(total_cost=total_cost)
        ) 
        for obj in objs:
            place = obj.price.place
            get_depo = obj.total_cost/2
            return Package.objects.update(
            price=place,deposit=get_depo
            )
            return depo 
            #self.deposit = get_depo
            #self.save()    
            
              
    def save(self,*args,**kwargs):
        super(Package,self).save(*args,**kwargs)
        
        
        
        
