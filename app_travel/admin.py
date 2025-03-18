from django.contrib import admin
from app_travel.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    deta_hierarchy = 'published_date'
    empty_value_display = '_empty_'
    fields = ["title","content", "image", "counted_views", "status", "published_date"]
    list_display = ["title", "status", "published_date", "created_date", "updated_date"]
    search_fields = ["title", "content"]
    list_filter = ["status", "published_date"]
    
admin.site.register(Post, PostAdmin)