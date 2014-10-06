from __future__ import(
absolute_import, unicode_literals
) 


import re 
from PIL import Image
from django.db import models
from django.db.models import *
from django.contrib import auth
from django.dispatch import receiver
from django.db.models.signals import *
from django.contrib.auth.models import *
from django.contrib.auth.signals import user_logged_in
from django.utils.encoding import smart_unicode


from django.db.models.manager import EmptyManager
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField


class CustomUserManager(BaseUserManager):
    def create_user(self, id_number, password=None, **extra_fields):
        now = timezone.now()
        if not id_number:
            raise ValueError('The given I.D number must be set')
        #email = UserManager.normalize_email(email)
        user = self.model(id_number=id_number,
                          is_staff=False,is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, id_number, password, **extra_fields):
        u = self.create_user(id_number, password, **extra_fields)
        u.is_admin = True
        u.save(using=self._db)
        return u
        

class CustomUser(AbstractBaseUser):
    id_number = models.CharField(
       max_length=50,unique=True,
       verbose_name='I.D Number'
    )
    full_name = models.CharField(
       max_length=50,
       verbose_name='Full Name'
    )
    photo = models.ImageField(
       upload_to='/profiles/photos',
       verbose_name='Profile Photo',
       null=True,blank=True
    )
    phone_number = models.IntegerField(
       verbose_name='Phone Number'
    )
    bio = HTMLField(
       max_length=350,verbose_name='Bio',
       null=True,blank=True
    )
    email = models.EmailField(
       max_length=75,null=True,
       blank=True
    )
    is_staff = models.BooleanField(
       default=False
    )
    is_superuser = models.BooleanField(
       default=False
    )
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
       auto_now_add=True
    )
    USERNAME_FIELD = 'id_number'
    REQUIRED_FIELDS = [
    'full_name','phone_number',
    ]
    
    objects = CustomUserManager()
    
    class Meta(object):
        db_table = 'CustomUser'
        verbose_name_plural = 'CustomUser'
        
    def __unicode__(self):
        return self.id_number
     
    
           
    def get_full_name(self):
        #the user is identified by their id_number
        return self.full_name
        
    def get_short_name(self):
        return self.full_name
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
        
    def save(self,*args,**kwargs):
        super(CustomUser,self).save(*args,**kwargs)
        



class About(models.Model):
    user = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       related_name='+'
    )
    main_photo = models.ImageField(
       upload_to='places',
       verbose_name='Main Photo'
    )
    what_we_do = HTMLField(
       max_length=350,verbose_name='What We Do'
    )
    who_we_are = HTMLField(
       max_length=350,verbose_name='Who We Are'
    )
    how_it_works = HTMLField(
       max_length=350,verbose_name='How It Works'
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'About'
        verbose_name_plural = 'About'
        
    def __unicode__(self):
        return smart_unicode(self.user)
        
    def save(self,*args,**kwargs):
        super(About,self).save(*args,**kwargs) 
    
    
class Faq(models.Model):
    user = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       related_name='+'
    )
    qstn = HTMLField(
       max_length=350,verbose_name='Question'
    )
    answer = HTMLField(
       max_length=350,verbose_name='Answer'
    )
    is_public = models.BooleanField(
       default=True
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'FAQ Item'
        verbose_name_plural = 'FAQ Items'
        
    def __unicode__(self):
        return u'%s %s' % (self.qstn,self.answer)
        
    def save(self,*args,**kwargs):
        super(Faq,self).save(*args,**kwargs)
    
    
class Message(models.Model):
    """emails"""
    from_email = models.EmailField(
       max_length=50
    )
    subject = models.CharField(
       max_length=50,null=True,
       blank=True
    )
    msg = HTMLField(
       max_length=450
    )
    reply = HTMLField(
       max_length=450,null=True,blank=True,
       verbose_name='Reply',
    )
    is_replied = models.BooleanField(
       default=False,
       verbose_name='Replied to'
    )
    date = models.DateTimeField(
       auto_now_add=True
    )
    class Meta(object):
        db_table = 'E-mail'
        ordering = ['date']
        verbose_name_plural = 'E-mails'
        
    def __unicode__(self):
        return self.subject
        
    def save(self,*args,**kwargs):
        super(Message,self).save(*args,**kwargs)
        
        

        
        
        
        
        



