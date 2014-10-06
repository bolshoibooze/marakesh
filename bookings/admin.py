from django.contrib import admin
from accounts.relatedfield_admin import *
from .models import *


class BookingMasterAdmin(admin.ModelAdmin):
    fieldsets = (
       ('Place',{
       'fields':('destination',)
       }),
       ('Personal Details',{
       'fields':('full_name','phone_number','id_number',)
       }),
       ('Booking',{
       'fields':('nights','checkin_date','special_request')
       }),
       ('FamilY/Group Booking',{
       'fields':('adults','children','under_5')
       }),
       ('Transaction Details',{
       'fields':('transaction_id','deposit')
       }),
    )
    list_display = ('full_name','phone_number','nights','checkin_date')
    list_filter = ('date','checkin_date')
    
admin.site.register(BookingMaster,BookingMasterAdmin)
    
