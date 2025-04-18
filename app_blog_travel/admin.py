from django.contrib import admin
from app_blog_travel.models import *

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    fields = ["name"]
    list_display = ["name"]
    
admin.site.register(Tag, TagAdmin)

class TagAuthor(admin.ModelAdmin):
    fields = ["name", "image", "about"]
    list_display = ["name","image", "about"]
    search_fields = ["name"]

admin.site.register(Author, TagAuthor)

class PostAdmin(admin.ModelAdmin):
    deta_hierarchy = 'published_date'
    empty_value_display = '_empty_'
    fields = ["title", "content", "slug","image", "counted_views", "Tags", "author", "published_date"]
    list_display = ["title", "published_date", "created_date", "updated_date"]
    search_fields = ["title", "content", "Tags"]
    list_filter = ["published_date", "Tags"]
    
admin.site.register(Post, PostAdmin)