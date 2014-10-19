from django.contrib import admin
from accounts.relatedfield_admin import *
from sorl.thumbnail.admin import AdminImageMixin
from .models import *


class CostingAdmin(admin.ModelAdmin):
    fieldsets = (
      
       ('Details',{
       'fields':('place','season','category','cost','start_date','end_date',)
       }),
       
    )
    list_display = ('place','season','category','cost')
    list_filter = ('season','place',)
    
admin.site.register(Costing,CostingAdmin)
    

class PackageAdmin(RelatedFieldAdmin):
    fieldsets = (
       ('Place & Category',{
       'fields':('price','category',)
       }),
       ('Number of Nights',{
       'fields':('nights',)
       }),
       ('Package Details',{
       'fields':('description',)
       }),
       ('Total Cost',{
       'fields':('total_cost',)
       })
    )
    list_display = ('price__place','nights','total_cost','deposit')
    list_filter = ('price__place',)
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
        
admin.site.register(Package,PackageAdmin)


class OtherPackageAdmin(admin.ModelAdmin):
    fieldsets = (
      ('Name & Cost',{
       'fields':('name','cost')
      }),
      ('Overview',{
       'fields':('overview',)
      }),
      ('Full Description',{
       'fields':('details',)
      }),
      ('Acitivities',{
       'fields':('activities',)
      }),
      ('Photos',{
       'fields':('photos',)
      }),
    )
    list_display = ('name','cost','date')
    list_filter = ('name',)
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
        
admin.site.register(OtherPackage,OtherPackageAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    fieldsets = (
       ('Registration Form',{
          'fields':('full_name','gender','phone_number','id_number','is_attending')
       }),
       #('Admin Actions',{'fields':('is_attending')}),
    
    )
    list_display = ('full_name','gender','male_count','female_count','totals')
    list_filter = ('id_number',)
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
        
admin.site.register(Participant,ParticipantAdmin)







    
    
