from django.urls import path
from app_travel.views import *

urlpatterns = [
    path('', index_view, name="index"),
    path('about', about_view, name="about"),
    path('blog-home', blog_home_view, name="home"),
    path('<slug:slug>/', blog_single_view, name="single"),
    path('elements', elements_view, name="elements"),
    path('contact', contact_view, name="contact"),
]