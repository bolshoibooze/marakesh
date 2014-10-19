from django.contrib import admin
from accounts.relatedfield_admin import *
from sorl.thumbnail.admin import AdminImageMixin
from .models import *


admin.site.register(CustomUser)

class AboutAdmin(admin.ModelAdmin):
    """
    fieldsets = (
       ('Photo',{'fields':('main_photo',)}),
       
       ('What We Do',{'fields':('what_we_do',)}),
       
       ('Who We Are',{'fields':('who_we_are',)}),
       
       ('How It Works',{'fields':('how_it_works')}),
    )
    """
    #list_display = ('date',)
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
        
admin.site.register(About,AboutAdmin)


class MessageAdmin(RelatedFieldAdmin):
    fieldsets = (
       ('E-mail Message',{
       'fields':('subject','msg','reply','is_replied',)
       }),
    )
    list_display = ('subject','is_replied','date')
    list_filter = ('date',)

    
        
admin.site.register(Message,MessageAdmin)



class FaqAdmin(admin.ModelAdmin):
    fieldsets = (
       ('Question & Answer',{
       'fields':('qstn','answer','is_public')
       }),
       
    )
    list_display = ('qstn','is_public','date')
    list_filter = ('is_public',)
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
        
admin.site.register(Faq,FaqAdmin)
