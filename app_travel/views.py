from django.shortcuts import render, get_object_or_404
from app_travel.models import *
from django.utils import timezone
from app_travel.forms import *
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def elements_view(request):
    return render(request, "elements.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "Unknown"
            contact.save()
            messages.success(request, "Your message has been sent successfully.")
        else:
            messages.error(request, "There was an error sending your message. Please try again.")
    form = ContactForm()
    return render(request, "contact.html", {'form': form})