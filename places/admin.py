from django.contrib import admin
from accounts.relatedfield_admin import *
from django.contrib.admin.widgets import AdminFileWidget
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.safestring import mark_safe
from sorl import thumbnail
from packages.models import *
from .models import *

    
class PlaceAdmin(RelatedFieldAdmin):
   fieldsets = (
      ('Place',{
      'fields':('name','location','main_photo','description','packages' )
      }),
      ('Additional Photos',{'fields':('photos',)}),
      #('Packages',{'fields':('package',)}),
      ('Booking & Availability',{
      'fields':('is_available','on_hold',)
      }),
      #('Availability',{'fields':('is_available','on_hold',)}),
      #('Terms & Conditions(optional)',{'fields':('terms')}),
   )
   list_display = ('name','location','is_available','on_hold')
   list_filter = ('location','name')
   #inlines = [PhotoAdminInline,]
   exclude = ('user',)
    
   def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
   
   
admin.site.register(Place,PlaceAdmin)




    




