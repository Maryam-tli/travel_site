from django.shortcuts import render, get_object_or_404
from app_travel.models import *
from django.utils import timezone

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def elements_view(request):
    return render(request, "elements.html")

def contact_view(request):
    return render(request, "contact.html")