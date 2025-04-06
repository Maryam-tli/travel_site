from django.shortcuts import render, get_object_or_404
from app_blog_travel.models import *
from django.utils import timezone

# Create your views here.
def blog_home_view(request, Tags_item=None):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if Tags_item:
        posts = posts.filter(Tags__name=Tags_item)
    all_tags = Tag.objects.filter(post__in=posts).distinct()
    
    context = {
        'posts': posts,
        'all_tags': all_tags,
    }
    return render(request, "blog-home.html", context)


def blog_single_view(request, slug):
    class_obj = get_object_or_404(Post, slug=slug)
    class_obj.counted_views += 1
    class_obj.save(update_fields=['counted_views'])
    posts = list(Post.objects.filter(published_date__lt=timezone.now()).order_by('-published_date'))
    
    try:
      index = posts.index(class_obj)
    except ValueError:
      index = -1

    if index<0:
        index = 0
    elif index >= len(posts):
        index = len(posts) - 1
    
    if index > 0:
        prev_post = posts[index - 1]
    else:
        prev_post = None
    if index < len(posts) - 1:
        next_post = posts[index + 1]
    else:
        next_post = None

    context = {
        'class_obj': class_obj,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog-single.html', context)