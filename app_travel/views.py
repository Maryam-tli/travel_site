from django.shortcuts import render, get_object_or_404
from app_travel.models import *
from django.utils import timezone

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def blog_home_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, "blog-home.html", context)


def blog_single_view(request, slug):
    class_obj = get_object_or_404(Post, slug=slug)
    class_obj.counted_views += 1
    context = {
        'class_obj': class_obj,
    }
    return render(request, 'blog-single.html', context)

def elements_view(request):
    return render(request, "elements.html")

def contact_view(request):
    return render(request, "contact.html")