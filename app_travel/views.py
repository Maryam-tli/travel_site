from django.shortcuts import render, get_object_or_404, redirect
from app_travel.models import *
from django.utils import timezone
from app_travel.forms import *
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import get_backends
from app_travel.backends import EmailOrUsernameModelBackend

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

def signup_view(request):
    form = CustomSignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            backend_found = False
            for backend in get_backends():
                if isinstance(backend, EmailOrUsernameModelBackend):
                    user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
                    backend_found = True
                    break
            login(request, user)  # ورود خودکار بعد از ثبت‌نام
            return redirect('/')  # یا هر صفحه‌ای که خواستی
    return render(request, 'signup.html', {'form': form})

def coming_soon(request):
    return render(request, 'coming_soon.html')