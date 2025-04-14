from django.contrib import admin
from app_travel.models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    search_fields = ['name', 'email']
    fields = ['name', 'email', 'subject', 'message']
    
admin.site.register(Contact, ContactAdmin)