from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def blog_home_view(request):
    return render(request, "blog-home.html")

def blog_single_view(request):
    return render(request, 'blog-single.html')

def elements_view(request):
    return render(request, "elements.html")

def contact_view(request):
    return render(request, "contact.html")