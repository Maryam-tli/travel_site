from django.urls import path
from app_blog_travel.views import *

app_name = 'app_blog_travel'

urlpatterns = [
    path('blog-home', blog_home_view, name="home"),
    path('<slug:slug>/', blog_single_view, name="single"),
]