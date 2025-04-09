from django.shortcuts import render, get_object_or_404
from app_blog_travel.models import *
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_home_view(request, Tags_item=None):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if Tags_item:
        posts = posts.filter(Tags__name=Tags_item)
        
    all_authors = Author.objects.all()

    all_tags = Tag.objects.filter(post__in=posts)

    tag_dict = {}

    for tag in all_tags:
        if tag.name not in tag_dict:
            tag_dict[tag.name] = 1
        else:
            tag_dict[tag.name] += 1
    paginator = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'blog-home.html', {'tag_dict': tag_dict, 'page_obj': page_obj, 'all_authors':all_authors,})


def blog_single_view(request, slug):
    class_obj = get_object_or_404(Post, slug=slug)
    class_obj.counted_views += 1
    class_obj.save(update_fields=['counted_views'])
    posts = list(Post.objects.filter(published_date__lt=timezone.now()).order_by('-published_date'))
    
    all_authors = Author.objects.all()
    
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
        'all_authors':all_authors,
    }
    return render(request, 'blog-single.html', context)

def blog_search_view(request, Tags_item=None):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if Tags_item:
        posts = posts.filter(Tags__name=Tags_item)

    if request.method == 'GET':
        posts = posts.filter(content__icontains=request.GET.get('search'))
    print(request.__dict__)
    
    context = {'posts': posts,}
    return render(request, 'blog-home.html', context)