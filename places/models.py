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


from packages.models import *
from photos.models import *

class Terms(models.Model):
    title = models.CharField(
       max_length=50,unique=True,
       verbose_name='Title',
       help_text='e.g,General,or Villa One'
    )
    post = HTMLField(
       max_length=500,
       verbose_name='Terms'
    )
    has_agreed = models.BooleanField(
       default=False
    )
    is_public = models.BooleanField(
       default=True
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'Terms & Conditions'
        verbose_name_plural = 'Terms & Conditions'
        
    def __unicode__(self):
        return self.is_public
        
    def save(self,*args,**kwargs):
        super(Terms,self).save(*args,**kwargs)
        

        

        
        
  
        
class Place(models.Model):
    name = models.CharField(
       db_index=True,max_length=50
    )
    location = models.CharField(
       max_length=250
    )
    main_photo = models.ImageField(
       upload_to='places',
       verbose_name='Main Photo'
    )
    description = HTMLField(
       max_length=160,
       verbose_name='Short Description'
    )
    full_description = HTMLField(
       max_length=250,null=True,blank=True,
       verbose_name='Full Description'
    )
    photos = models.ForeignKey(
       PhotoAlbum,related_name='+',
       verbose_name = 'Photos',
       null=True,blank=True
    )
    packages = models.ForeignKey(
       Package,related_name='p',
       verbose_name='Package',
       null=True,blank=True
    )
    terms = models.ForeignKey(
        Terms,related_name='+',
        null=True,blank=True
    )
    reviews = models.ForeignKey(
       'self',related_name='review',
        null=True,blank=True
    )
    on_hold = models.BooleanField(
       default=False
    )
    is_available = models.BooleanField(
       default=True
    )
    user = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       related_name='+'
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'Holiday Site'
        ordering = ['date','is_available']
        verbose_name_plural = 'Holiday Sites'
        
        
    def __unicode__(self):
        return self.name
        
    def save(self,*args,**kwargs):
        super(Place,self).save(*args,**kwargs)    
        
       
  
 
