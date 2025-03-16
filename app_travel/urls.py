from django.urls import path
from app_travel.views import *

urlpatterns = [
    path('', index_view, name="index"),
    path('/about', about_view, name="about"),
    path('/blog-home', blog_home_view, name="home"),
    path('/blog-single', blog_single_view, name="single"),
]