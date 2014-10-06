from __future__ import(
absolute_import, unicode_literals
) 

import datetime
from PIL import Image 
from django.db import models
from django.db.models import *
from django.contrib import auth
from django.utils.encoding import smart_unicode



        
        
class PhotoAlbum(models.Model):
    title = models.CharField(
       max_length=50,unique=True,
       verbose_name='Name of Hotel'
    )
    image = models.ImageField(
       upload_to='site/photos',
       verbose_name='Photo'
    )
    image_2 = models.ImageField(
       upload_to='site/photos',
       verbose_name='Photo'
    )
    image_3 = models.ImageField(
       upload_to='site/photos',
       verbose_name='Photo'
    )
    image_4 = models.ImageField(
       upload_to='site/photos',
       verbose_name='Photo'
    )
    image_5 = models.ImageField(
       upload_to='site/photos',
       null=True,blank=True,
       verbose_name='Photo'
    )
    image_6 = models.ImageField(
       upload_to='site/photos',
       null=True,blank=True,
       verbose_name='Photo'
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'Photo Item'
        ordering = ['-date']
        verbose_name_plural = 'Photos Items'
        
        
    def __unicode__(self):
        return smart_unicode(self.image)

    def save(self,*args,**kwargs):
        super(PhotoAlbum,self).save(*args,**kwargs)     
