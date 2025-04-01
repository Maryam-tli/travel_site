from django.urls import path
from app_travel.views import *

app_name = 'app_travel'

urlpatterns = [
    path('', index_view, name="index"),
    path('about', about_view, name="about"),
    path('elements', elements_view, name="elements"),
    path('contact', contact_view, name="contact"),
]