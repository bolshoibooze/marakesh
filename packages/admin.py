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
    
    
