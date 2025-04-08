from django import template
from django.utils import timezone
from app_blog_travel.models import *

register = template.Library()

@register.inclusion_tag('includ_latest_blog.html')
def latest_blog():
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    return {'posts': posts,}