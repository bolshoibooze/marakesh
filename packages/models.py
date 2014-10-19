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
from photos.models import *



       
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
        
        
class OtherPackage(models.Model):
    name = models.CharField(
       max_length = 50,
       verbose_name='Package Title'
    )
    cost = models.CharField(
       max_length=50,null=True,blank=True,
       verbose_name = 'Average Cost'
    )
    overview = HTMLField(
       max_length=140,
       verbose_name = 'Brief Overview',
       help_text='140 words max'
    )
    details = HTMLField(
       max_length=500,
       verbose_name = 'Full Description',
       help_text='500 words max'
    )
    photos = models.ManyToManyField(
       PhotoAlbum,related_name='+',
       verbose_name='Optional:Photos',
       null=True,blank=True
    )
    activities = HTMLField(
       max_length=500,
       verbose_name = 'Activities'
    )
    user = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       related_name='+'
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'Other Package'
        ordering = ['-date']
        verbose_name_plural = 'Other Packages'
        
    def __unicode__(self):
        return self.name 
        
    @permalink
    def get_absolute_url(self):
        return ('otherpackage',{'slug': self.slug})
           
    def save(self,*args,**kwargs):
        super(OtherPackage,self).save(*args,**kwargs)
        
        

        
        

class Participant(models.Model):
    package = models.ForeignKey(
       OtherPackage,related_name='+',
       verbose_name='Select Package'
    )
    full_name = models.CharField(
       max_length=50
    )
    gender =  models.CharField(
       max_length=100,
       choices = settings.GENDER,
       verbose_name='Gender',  
    )
    phone_number = models.IntegerField(
       verbose_name='Main Phone Number'
    )
    id_number = models.IntegerField(
       verbose_name='Id Number'
    )
    is_attending = models.BooleanField(
       default=False
    )
    status = models.BooleanField(
       default=False,
       verbose_name='Tick if sold out'
    )
    male_count = models.IntegerField(
       default=0
    )
    female_count = models.IntegerField(
       default=0
    )
    totals = models.IntegerField(
       default=0
    )
    user = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       related_name='+',null=True,
       blank=True
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'Participant'
        ordering = ['-date']
        verbose_name_plural='Participants'
        
    def __unicode__(self):
        return smart_unicode(self.package)
        
        
    def save(self,*args,**kwargs):
        super(Participant,self).save(*args,**kwargs)
    
        
        
        
        
        
        
        
