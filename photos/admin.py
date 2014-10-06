from django.contrib import admin
from accounts.relatedfield_admin import *
from .models import *

class PhotoAlbumAdmin(admin.ModelAdmin):
    fieldsets = (
       ('Required Photos',{
       'fields':('title','image','image_2','image_3','image_4')
       }),
       ('Additional Photos(optional)',{
       'fields':('image_5','image_6',)
       }),
    )
    list_display = ('title','date',)
    list_filter = ('date',)
    
        
admin.site.register(PhotoAlbum,PhotoAlbumAdmin)
