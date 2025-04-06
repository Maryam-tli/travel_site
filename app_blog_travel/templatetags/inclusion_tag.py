from django import template
from django.utils import timezone
from app_blog_travel.models import *

register = template.Library()

@register.inclusion_tag('inclusion_page.html')
def popular_posts():
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return {'posts': posts}